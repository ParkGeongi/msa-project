from django.urls import re_path as url

from movie.movies import views


from django.urls import re_path as url

from movie.theaters import views

urlpatterns = [
    url(r'theater',views.theater),
    url(r'list',views.theater_list)
]