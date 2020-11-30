from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/',views.logout,name='logout'),
    # path('', views.dashboard, name='dashboard'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('account_signup', views.register, name='account_signup'),
    # path('add_data',views.personal_view,name='personal_data'),
    # path('search_data',views.search_view,name='search'),
    # path('full_data',views.full_details,name='full_data'),
    #
    # url(r'^update/(?P<pk>\d+)/$',views.edit,name='personal_edit'),
    # url(r'^det/(?P<pk>\d+)/$',views.det,name='det'),
    # url(r'^full_data/(?P<pk>\d+)/$',views.full_data,name='full_data_details'),
    # path('invitations/send-invite',views.send_invite)
    # path('refer',views.refer,name='refer')












]