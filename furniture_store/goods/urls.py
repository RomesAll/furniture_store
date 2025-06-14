from django.contrib import admin
from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:slug>/', views.CatalogView.as_view(), name='catalog'),
    path('product/<slug:slug>', views.ProductView.as_view(), name='product'),
]