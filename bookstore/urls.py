from django.conf.urls import url
from django.urls import path
from bookstore.views import BookCreate, BookDelete, BookGet, BookList, BookUpdate, UploadBook

urlpatterns = [
    path('list/', BookList.as_view(), name='list'),
    path('create/', BookCreate.as_view(), name='create'),
    path("upload-csv/", UploadBook.as_view(), name='upload'),
    url(r'^(?P<id>\d+)/$', BookGet.as_view(), name='view'),
    url(r'^(?P<id>\d+)/edit/$', BookUpdate.as_view(), name='edit'),
    url(r'^(?P<id>\d+)/delete/$', BookDelete.as_view(), name='delete'),
]
