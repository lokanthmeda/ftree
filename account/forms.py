# import re
#
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext as _
#
#
# class NumberValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('\d', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 digit, 0-9."),
#                 code='password_no_number',
#             )
#
#     def get_help_text(self):
#         return _(
#             "Your password must contain at least 1 digit, 0-9."
#         )
#
#
# class UppercaseValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('[A-Z]', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 uppercase letter, A-Z."),
#                 code='password_no_upper',
#             )
#
#     def get_help_text(self):
#         return _(
#             "Your password must contain at least 1 uppercase letter, A-Z."
#         )
#
#
# class LowercaseValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('[a-z]', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 lowercase letter, a-z."),
#                 code='password_no_lower',
#             )
#
#     def get_help_text(self):
#         return _(
#             "Your password must contain at least 1 lowercase letter, a-z."
#         )
#
#
# class SymbolValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 symbol: " +
#                   "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
#                 code='password_no_symbol',
#             )
#
#     def get_help_text(self):
#         return _(
#             "Your password must contain at least 1 symbol: " +
#             "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
#         )

from django import forms
from django.contrib.auth.models import User
from django_countries.widgets import CountrySelectWidget
#
# from .models import Personal_data, Referal
from django.core.exceptions import ValidationError

def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError("Email address %s already exists, must be unique" % value)


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(required=True, validators=[validate_email_unique])
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

#
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class DataForm(forms.ModelForm):
#     class Meta:
#         model = Personal_data
#         fields = ('first_name', 'last_name', 'date_of_birth', 'city','country', 'photo','relation','gender')
#         widgets = {'country':CountrySelectWidget(),
#                    'relation':forms.RadioSelect()}
#
# #
# class relationForm(forms.ModelForm):
#     class Meta:
#         model = Referal
#         fields = 'relation',


# from .models import RR
# from invitations.models import Invitation
# class rrform()