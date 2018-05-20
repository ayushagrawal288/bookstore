from django.db import models
from datetime import date
from rest_framework import fields
# from rest_framework.models import
# fields.ModelField
# from rest_framework.utils.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, related_name='book', on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, related_name='book')
    edition = models.CharField(max_length=30, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    data_published = models.DateField(default=date.today)
