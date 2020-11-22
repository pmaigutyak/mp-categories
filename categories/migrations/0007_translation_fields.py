# Generated by Django 3.0.10 on 2020-11-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(blank=True, max_length=4096, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_uk',
            field=models.TextField(blank=True, max_length=4096, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Category name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Category name'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Category title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uk',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Category title'),
        ),
    ]
