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

from .models import Personal_data, Referal
from django.core.exceptions import ValidationError

class DataForm(forms.ModelForm):
    class Meta:
        model = Personal_data
        fields = ('first_name', 'last_name', 'date_of_birth', 'city','country', 'photo','relation','gender')
        widgets = {'country':CountrySelectWidget(),
                   'relation':forms.RadioSelect()}

#
class relationForm(forms.ModelForm):
    class Meta:
        model = Referal
        fields = 'relation',


# from .models import RR
# from invitations.models import Invitation
# class rrform()