# Generated by Django 4.2.7 on 2023-11-10 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_main_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ads',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]