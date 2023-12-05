from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
   ('real_estate', 'Недвижимость'),
    ('transport', 'Транспорт'),
    ('home_and_garden', 'Товары для дома и сада'),
    ('electronics', 'Электроника'),
    ('clothing_and_footwear', 'Одежда и обувь'),
    ('services', 'Услуги'),
    ('pets', 'Животные'),
    ('sports_and_hobbies', 'Спорт и хобби'),
    ('business_and_equipment', 'Бизнес и оборудование'),
    ('food_and_drinks', 'Продукты и напитки'),   
)
    


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Название категории", help_text= "Категория, к которой принадлежит продукт")
    main_category = models.CharField(max_length=100,choices=CATEGORY_CHOICES, default = "real_estate", verbose_name = "Главная категория", help_text= "Главная категория")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    

class Ads(models.Model):
    image = models.ImageField(upload_to ="ads/", verbose_name = "Изображение", help_text= "Добавьте фотографию")
    title = models.CharField(max_length=100, verbose_name = "Название продукта", help_text= "Напишите название вашего продукта")
    description = models.TextField(verbose_name = "Описание", max_length = 999, help_text= "Описание продукта ...")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name = "Цена")
    contact = models.CharField(max_length=100, verbose_name = "Связь")
    address = models.CharField(max_length=255, verbose_name = "Адрес")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Категория", help_text= "Укажите категорию вашего продукта")
    whatsapp = models.URLField(verbose_name = "ссылка на WhatsApp", blank=True, null=True)
    telegram = models.URLField(verbose_name = "ссылка на Telegram", blank=True, null=True)
    instagram = models.URLField(verbose_name = "ссылка на Instagram", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Пользователь", help_text= "Пользователь, разместивший объявление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания")
    
    def __str__(self):
        return f"{self.title} - {self.user.username}" 
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
