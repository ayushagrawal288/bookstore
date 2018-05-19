from django.conf.urls import url
from django.urls import path
from bookstore.views import BookCreate, BookDelete, BookGet, BookList, BookSearch, BookUpdate

urlpatterns = [
    url(r'^list/$', BookList.as_view(), name='list'),
    url(r'^find$', BookSearch.as_view(), name='find'),
    url(r'^create/$', BookCreate.as_view(), name='create'),
    path('view/<id>/', BookGet.as_view(), name='view'),
    path('view/<id>/edit', BookUpdate.as_view(), name='edit'),
    path('view/<id>/delete', BookDelete.as_view(), name='delete')
]
