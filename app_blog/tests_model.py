from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/articles/category/innovations')