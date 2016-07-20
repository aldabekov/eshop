from __future__ import unicode_literals


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name')
    alias = models.SlugField(verbose_name='Alias categories')

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Item name')
    price = models.IntegerField(default=0, verbose_name='Price')
    image = models.ImageField(upload_to='media', blank=True, verbose_name='Url on image')
    alias = models.SlugField(verbose_name='Alias items')
    category = models.ForeignKey(Category, related_name='items')

    class Meta:
        verbose_name_plural = 'Items'

    def __unicode__(self):
        return self.name

class AboutUs(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='About Us Page'