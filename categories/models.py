
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from slugify import slugify_url


class Category(models.Model):

    name = models.CharField(
        _('Category name'),
        max_length=255)

    title = models.CharField(
        _('Category title'),
        max_length=255,
        blank=True)

    logo = models.ImageField(
        _('Logo'),
        upload_to='categories',
        blank=True,
        null=True,
        max_length=255)

    code = models.CharField(
        _('Code'),
        max_length=255,
        blank=True)

    icon = models.CharField(
        _('Icon'),
        max_length=255,
        blank=True)

    description = models.TextField(
        _('Description'),
        blank=True,
        max_length=4096)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('products:list', args=[self.slug, self.id])

    @property
    def slug(self):
        return slugify_url(self.name or 'category', separator='_')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class CategoryField(models.ForeignKey):

    def __init__(
            self,
            to='categories.Category',
            verbose_name=_('Category'),
            on_delete=models.CASCADE,
            *args, **kwargs):

        super(CategoryField, self).__init__(
            to,
            verbose_name=verbose_name,
            on_delete=on_delete,
            *args, **kwargs)
