from __future__ import unicode_literals
import csv
import codecs
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter
from bookstore.serializers import BookSerializer
from bookstore.models import Book
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from bookstore.utils import get_modal_fields
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError


class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'author__name', 'publisher__name')


class BookCreate(CreateAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        publisher_data = request.data.pop('publisher', None)
        author_data = request.data.pop('author', [])

        if isinstance(publisher_data, str):
            request.data.update({'publisher': {'name': publisher_data}})

        author_list = list()
        if isinstance(author_data, str):
            author_list.append({'name': author_data})
        else:
            for data in author_data:
                if isinstance(data, str):
                    author_list.append({'name': data})
                else:
                    author_list.append(data)
        request.data['author'] = author_list

        try:
            return self.create(request, *args, **kwargs)
        except (ValidationError, KeyError) as e:
            return Response({'error': e.__str__()})


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


class UploadBook(GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def create(self, data):
        publisher_data = data.get('publisher')
        author_data = data.get('author')

        if publisher_data:
            data.update({'publisher': {'name': publisher_data}})

        author_list = list()
        if isinstance(author_data, str):
            author_list.append({'name': author_data})
        else:
            for data in author_data:
                if isinstance(data, str):
                    author_list.append({'name': data})
                else:
                    author_list.append(data)
        data['author'] = author_list

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return

    def get(self, request):
        return render(request, "test.html", {})

    def post(self, request):
        try:
            csvfile = request.FILES['csv_file']
        except MultiValueDictKeyError:
            return Response({"message": "no input file"})

        if not csvfile.name.endswith('.csv'):
            return Response({'message': "input file must be of type csv"})

        data = csv.reader(codecs.iterdecode(csvfile, 'utf-8'))
        data = list(data)
        attr = data[0]
        fields = get_modal_fields(Book)
        for i in range(1, len(data)):
            book_doc = {attr[j].lower(): data[i][j] for j in range(len(attr)) if attr[j].lower() in fields}
            try:
                self.create(book_doc)
            except (ValidationError, KeyError) as e:
                return Response({'error': e.__str__()})
        return Response({'success': True})
