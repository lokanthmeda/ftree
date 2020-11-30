# from django.test import TestCase
# from .models import Personal_data
# from django.urls import reverse
# from .forms import DataForm
#
# class EverTest(TestCase):
#     def create_whatever(self,user=1,first_name='meda',last_name='chinna',gender='male',
#                         date_of_birth=03-03-4322,):
#     def test_EverTest(self):
#         i=Personal_data.objects.get(id=1)
#         self.assertTrue(isinstance(i,Personal_data))
#         self.assertEqual(i.__unicode__(),i.first_name)
from django.test import TestCase

from .models import Personal_data

class AuthorModelTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     # Set up non-modified objects used by all test methods
    #     Personal_data.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        # author = Personal_data.objects.get(id=1)
        # field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(Personal_data.objects.get(id=1), 'first_name')

    # def test_date_of_death_label(self):
    #     author=Author.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_death').verbose_name
    #     self.assertEqual(field_label, 'died')
    #
    # def test_first_name_max_length(self):
    #     author = Personal_data.objects.get(id=1)
    #     max_length = author._meta.get_field('first_name').max_length
    #     self.assertEqual(max_length, 20)
    #
    # def test_object_name_is_last_name_comma_first_name(self):
    #     author = Author.objects.get(id=1)
    #     expected_object_name = f'{author.last_name}, {author.first_name}'
    #     self.assertEqual(expected_object_name, str(author))
