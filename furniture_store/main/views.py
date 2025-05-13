from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpRequest, HttpResponse
from goods.models import Categories, Product

# Create your views here.
class Index(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['content'] = 'Магазин мебели HOME'
        return context

    
#Views about 
class About(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['content'] = 'Текст о том какой классный этот интернет магазин.'
        return context