from __future__ import unicode_literals
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter
from bookstore.serializers import BookSerializer
from bookstore.models import Book


class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        import pdb
        pdb.set_trace()
        return data


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
