from django.db import models

# Create your models here.
class Categories(models.Model):
    
    name = models.CharField(max_length=100, 
                            verbose_name='Название',
                            unique=True)
    slug = models.SlugField(verbose_name='Slug', 
                            max_length=100, unique=True, 
                            blank=True, null=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    
    name = models.CharField(max_length=100, 
                            verbose_name='Название',
                            unique=True)
    slug = models.SlugField(verbose_name='Slug', 
                            max_length=100, unique=True, 
                            blank=True, null=True)
    
    description = models.TextField(blank=True,null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
    
    def display(self):
        return f'{self.id:05}'
    
    def discount_price(self):
        return round(self.price - (self.price * self.discount / 100),2)
    


