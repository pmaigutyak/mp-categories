# Generated by Django 2.0.13 on 2020-07-29 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]