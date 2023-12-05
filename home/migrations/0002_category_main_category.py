# Generated by Django 4.2.7 on 2023-11-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.CharField(choices=[('real_estate', 'Недвижимость'), ('transport', 'Транспорт'), ('home_and_garden', 'Товары для дома и сада'), ('electronics', 'Электроника'), ('clothing_and_footwear', 'Одежда и обувь'), ('services', 'Услуги'), ('pets', 'Животные'), ('sports_and_hobbies', 'Спорт и хобби'), ('business_and_equipment', 'Бизнес и оборудование'), ('food_and_drinks', 'Продукты и напитки')], default='real_estate', help_text='Главная категория', max_length=100, verbose_name='Главная категория'),
        ),
    ]