# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
# from django.shortcuts import render
from rest_framework.filters import SearchFilter
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from bookstore.serializers import BookSerializer, PublisherSerializer, AuthorSerializer
from bookstore.models import Book, Author, Publisher
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreate(CreateAPIView):
    serializer_class = BookSerializer


class BookUpdate(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_url_kwarg = 'id'


class BookGet(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_url_kwarg = 'id'


class BookDelete(DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_url_kwarg = 'id'


class BookSearch(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'author__name', 'publisher__name')
