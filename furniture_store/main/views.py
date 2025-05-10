from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpRequest, HttpResponse


# Create your views here.
class Index(TemplateView):
    template_name = 'main/index.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['content'] = 'Главная страцниа магазина Home'
        return context
    

class About(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello word')