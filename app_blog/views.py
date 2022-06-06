# app_blog/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


# Створіть свої представлення тут.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
