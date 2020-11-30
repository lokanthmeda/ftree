# from urllib import request
from django.utils.timezone import timezone
from django.contrib.auth.models import User
from django.db import models
from django.http import request
from django_countries.fields import CountryField
from django_countries import Countries, countries
from django.conf import settings
class Personal_data(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Personal_data')
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    parents_lastname = models.CharField(max_length=20,blank=True)
    gender_choices = (
        ('male','MALE'),
        ('female','FEMALE')
    )
    gender=models.CharField(max_length=7,choices=gender_choices)
    date_of_birth = models.DateField(blank=True, null=True)
    city=models.CharField(max_length=20)
    country=CountryField(choices=list(countries))
    photo = models.ImageField(blank=True,upload_to='media',null=True)
    relation_choices=(
        ('self','SELF'),
        ('mother','MOTHER'),
        ('father',"FATHER"),
        ('brother','BROTHER'),
        ('sister','SISTER'),
        ('son','SON'),
        ('daughter','DAUGHTER'),
        ('husband','HUSBAND'),
        ('wife','WIFE')
    )
    relation=models.CharField(max_length=20,choices=relation_choices)
    parent_id = models.IntegerField(null=True,blank=True)
    referal_relation = models.CharField(max_length=20,blank=True,null=True)
    # created_at = models.DateTimeField(auto_now=True)
    # modified = models.DateTimeField(auto_now_add=True)


# from invitations.models import Invitation
# class RR(models.Model):
#     inv = models.ForeignKey(Invitation,on_delete=models.CASCADE,related_name=RR)
#     relative_name =models.CharField(max_length=20)

class Referal(models.Model):
    relation = models.CharField(max_length=20)
