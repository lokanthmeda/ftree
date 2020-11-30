from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from familytree.settings import EMAIL_HOST_USER
from .forms import DataForm, relationForm

from django.contrib.auth.decorators import login_required
from .models import Personal_data,Referal
from invitations.models import Invitation
from django.db.models import Q

#
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=True)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             # print('hello')
#             subject = 'Welcome to FamilyTree'
#             message = 'Thanks for registered with us '
#             recepient = str(user_form['email'].value())
#             send_mail(subject,
#                       message, EMAIL_HOST_USER, [recepient], fail_silently=False)
#
#             # messages.success(request, 'Account crreated successfully')
#             messages.success(request, 'Account Created Successfully')
#
#
#             return render(request, 'registration/login.html', {'new_user': new_user})
#         else:
#             user_form = UserRegistrationForm()
#             messages.success(request, 'Error occure in email or password')
#
#             return render(request, 'account/register.html', {'user_form': user_form})
#     else:
#         user_form = UserRegistrationForm()
#         return render(request, 'account/register.html', {'user_form': user_form})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#         return render(request, 'account/login.html', {'form': form})
#

@login_required
def details(request, pk):
    data = User.objects.get(id=pk)
    return render(request, 'account/details.html', {'data': data})


@login_required
def personal_view(request):
    # print(da)

    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')
        city = request.POST.get('city')
        country = request.POST.get('country')
        pic = request.POST.get('photo')
        gender = request.POST.get('gender')
        relation = request.user.username+request.POST.get('relation')
        rr = request.user.username + request.POST.get('referal_relation')
        # p_form = DataForm(request.POST,request.FILES)
        # # if p_form.is_valid():
        #     f_name = p_form.cleaned_data['first_name']
        #     l_name = p_form.cleaned_data['last_name']
        #     dob = p_form.cleaned_data['date_of_birth']
        #     city = p_form.cleaned_data['city']
        #     country = p_form.cleaned_data['country']
        #     pic = p_form.cleaned_data['photo']
        #     gender = request.POST['gender']
        #     relation = p_form.cleaned_data['relation']


        if not Personal_data.objects.filter(first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                date_of_birth=request.POST['date_of_birth']).exists():
            if relation == 'self':
                print(request.user.email)
                    # if request.user.email in Invites.objects.values_list('sentto_mailid', flat=True):
                if Invitation.objects.filter(email=request.user.email):
                    print("Hi")
                    da = Invitation.objects.filter(email=request.user.email)
                    for i in da:
                        k=i.id
                        print(i.id)
                    id = Invitation.objects.values_list('inviter_id', flat=True).get(email=request.user.email)
                    user_id = id

                    # relation = Referal_Relation.objects.values_list('relation', flat=True).get(
                    #         id=k)
                    print(relation)
                    k=Personal_data.objects.filter(user_id=request.user.id, relation=rr).values('id')
                    for j in k:
                        print(j.id,'juiu')

                    data = Personal_data(
                            user_id=user_id,
                            first_name=f_name,
                            last_name=l_name,
                            gender=gender,
                            date_of_birth=dob,
                            city=city,
                            country=country,
                            photo=pic,
                            relation=rr,
                            parent_id = request.user.id,
                            referal_relation = rr
                            # parent_id = Personal_data.objects.last().id
                        )
                    data.save()

                    return redirect('dashboard')
                else:

                    data = Personal_data(
                            user_id=request.user.id,
                            first_name=f_name,
                            last_name=l_name,
                            gender=gender,
                            date_of_birth=dob,
                            city=city,
                            country=country,
                            photo=pic,
                            relation=request.user.username + relation,
                            parent_id = Personal_data.objects.last().id,
                            referal_relation = rr

                        )

                    data.save()




                    return redirect('dashboard')


            else:
                # print(da)
                data = Personal_data(
                        user_id=request.user.id,
                        first_name=f_name,
                        last_name=l_name,
                        gender=gender,
                        date_of_birth=dob,
                        city=city,
                        country=country,
                        photo=pic,
                        relation=relation,
                        parent_id= Personal_data.objects.filter(parent_id=request.user.id,relation='self').values('id'),
                    referal_relation = rr



                    )

                data.save()
                print(data.parent_id)


                return redirect('dashboard')
        else:
            messages.success(request, 'You all ready Entered the same details')
            return render(request, 'account/data.html')
    else:
            # p_form = DataForm()
        return render(request, 'account/data.html')

    # else:
    #     return render(request, 'account/data.html')


@login_required
def edit(request, pk):
    if request.method == 'POST':
        p_form = DataForm(request.POST)
        if p_form.is_valid():
            f_name = p_form.cleaned_data['first_name']
            l_name = p_form.cleaned_data['last_name']
            dob = p_form.cleaned_data['date_of_birth']
            city = p_form.cleaned_data['city']
            country = p_form.cleaned_data['country']
            pic = p_form.cleaned_data['photo']
            gender = request.POST['gender']
            relation = p_form.cleaned_data['relation']
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')
        city = request.POST.get('city')
        country = request.POST.get('country')
        pic = request.POST.get('photo')
        gender = request.POST.get('gender')
        relation = request.POST.get('relation')
        rr = request.POST.get('referal_relation')
        data = Personal_data.objects.filter(id=pk)
        if data:
            data.update(
                        user_id=request.user.id,
                        first_name=f_name,
                        last_name=l_name,
                        gender=gender,
                        date_of_birth=dob,
                        city=city,
                        country=country,
                        photo=pic,
                        relation=relation,
                        # referal_relation = rr
                    )

            return redirect('dashboard')
    else:
        p_form = DataForm(instance=Personal_data.objects.get(id=pk))
        return render(request, 'account/data.html',{'p_form':p_form})


def search_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)

        fdata = Personal_data.objects.filter(first_name=search_query)

        if len(fdata) != 0:

            return render(request, 'data.html', {'data': fdata})
        else:
            return HttpResponse('Not Found')






@login_required
def dashboard(request):
    bdata = Personal_data.objects.filter(user_id=request.user.id)
    pdata = Personal_data.objects.filter(parent_id = request.user.id)
    # for i in bdata:
    #     print(i)
    # import csv
    # with open('lok.csv', 'w+', newline='') as file:
    #     writer = csv.writer(file)
    #
    #     writer.writerow(['ID','first_name','gender','relation','user_id'])
    #     for i in bdata:
    #         writer.writerow([i.id,i.first_name,i.gender,i.relation,i.user_id])
        # for i in range(bdata):
        #     print(i)
        #     writer.writerow(i)
    # print(request.user.id)
    # for i in bdata:
    #     print(i.user_id)
    return render(request, 'account/dashboard.html', {'bdata': bdata , 'pdata':pdata})



@login_required
def full_details(request):
    # # bdata = Personal_data.objects.filter(user_id = request.user.id)
    # # print("Hi")
    # if Invites.objects.filter(sentby=request.user.id):
    #
    #     dat = Invites.objects.filter(sentby=request.user.id)
    #     l=[]
    #     for j in dat:
    #         k=j.sentto_mailid
    #         print(k)
    #         da = User.objects.filter(email=k)
    #         # print('g')
    #         for a in da:
    #
    #             p=a.id
    #             # print(p)
    #         l.append(a.id)
    #     # print(l)
    #
    #
    #     my_filter_qs = Q()
    #     for i in l:
    #         my_filter_qs = my_filter_qs | Q(user_id=i)
    #     badata = Personal_data.objects.filter(my_filter_qs)
    #     print(badata)
    #
    #     data = Personal_data.objects.filter(user_id=request.user.id)
    #     return render(request, 'account/dash.html', {'badata':badata, 'bdata':data})
    # else:
    #     return HttpResponse('no')

    dat = Invitation.objects.values_list('email', flat=True).filter(inviter_id=request.user.id)
    print(dat)
    T = []
    while (True):
        P = list(User.objects.values_list('id', flat=True).filter(email__in=dat))
        T.extend(P)
        print(P)
        if Invitation.objects.filter(inviter_id__in=P):
            dat = Invitation.objects.values_list('email', flat=True).filter(inviter_id__in=P)
        else:
            break
    T.append(request.user.id)
    print(P)

    Q = Personal_data.objects.filter(user_id__in=T).order_by('user_id')
    for i in Q:
        print(i.first_name)
    # a=Personal_data.objects.filter(parent_id = request.user.id)
    return render(request, 'account/dash.html', {'results': Q})


def full_data(request,pk):
    data = Personal_data.objects.filter(user_id=pk)
    return render(request,'fd.html',{'data':data})

def det(request,pk):
    data = Personal_data.objects.filter(user_id=pk)
    return render(request,'fd.html',{'data':data})

def send_invite(request):
    return HttpResponse('working')