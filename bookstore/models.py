# from datetime import datetime
# from userSetup.models import UserInfo
# from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date
# from django.contrib.postgres.fields import ArrayField
# from rest_framework.serializers import ModelSerializer


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
    isbn = models.CharField(max_length=30)
    publisher = models.ForeignKey(Publisher, related_name='book', on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, related_name='book')
    edition = models.IntegerField(blank=True, null=True)
    data_published = models.DateField(default=date.today)
