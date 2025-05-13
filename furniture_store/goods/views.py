from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Categories, Product
from django.core.paginator import Paginator

# Create your views here.
class CatalogView(ListView):
    template_name = 'goods/catalog.html'
    model = Product
    context_object_name = 'post'
    paginate_by = 1

    def get_queryset(self):
        slug_obj = self.kwargs.get('slug', None)
        
        if slug_obj == 'all' or slug_obj is None:
            return Product.objects.all()
        
        categories_obj = get_object_or_404(Categories, slug=slug_obj)
        return Product.objects.filter(category_id=categories_obj.pk)
        

class ProductView(DetailView):
    template_name = 'goods/product.html'
    model = Product
    slug_url_kwarg = 'slug'
    context_object_name = 'product_detail'

    def get_object(self, queryset = None):
        return get_object_or_404(Product, slug=self.kwargs.get('slug',None))