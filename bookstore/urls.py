from django.conf.urls import url
from django.urls import path
from bookstore.views import BookCreate, BookDelete, BookGet, BookList, BookUpdate

urlpatterns = [
    url(r'^list$', BookList.as_view(), name='list'),
    url(r'^create$', BookCreate.as_view(), name='create'),
    path('<id>', BookGet.as_view(), name='view'),
    path('<id>/edit', BookUpdate.as_view(), name='edit'),
    path('<id>/delete', BookDelete.as_view(), name='delete')
]
