from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Category(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    title = models.CharField(max_length=100, verbose_name='Название Категории', help_text='введите название Категория')
    description = models.CharField(max_length=500, verbose_name='Описание')

    # возвращение дефолтного значения при обращении к обьекту

    def __str__(self):
        return self.title

    # Изменение заголовка модели в админке
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Dish(models.Model):
    image = models.ImageField(upload_to='images', null=True, verbose_name="Image", max_length=900)
    title = models.CharField(max_length=100, verbose_name="Meal Name", help_text="enter meal name")
    dish_type = models.CharField(max_length=100, verbose_name="Meal Type", help_text="enter meal type")
    description = models.CharField(max_length=500, verbose_name="Description", help_text="enter description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Блюдо')
        verbose_name_plural = ('Блюда')

class Beverage(models.Model):
    image = models.ImageField(upload_to='images', null=True, verbose_name="Картинка")
    title = models.CharField(max_length=100, verbose_name="название напитка", help_text="введите название напитка")
    beverages_type = models.CharField(max_length=100, verbose_name="тип напитка", help_text="введите тип напитка")
    description = models.CharField(max_length=500, verbose_name="Описание", help_text="введите описание напитка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Напиток')
        verbose_name_plural = ('Напитки')

class Cart(models.Model):
    session_key = models.CharField(max_length=999, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_cost = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    def get_total(self):
        items = CartContent.objects.filter(cart=self.id)
        total = 0
        for item in items:
            total += item.product.price * item.qty
        return total

class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Dish, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=True)