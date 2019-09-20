from django.conf.urls import url, include
from .views import *
from django.urls import path

app_name = "libraryapp"

urlpatterns = [
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^libraries$', list_libraries, name='libraries'),
    url(r'^library/form$', library_form, name='library_form'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^logout/$', logout_user, name='logout'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('libraries/<int:library_id>/', library_details, name='library'),
]

# path('books/<int:book_id>/', book_details, name='book'),
# from django.urls import path