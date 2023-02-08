from django.urls import re_path as url

from movie.movies import views


from django.urls import re_path as url

from movie.showtimes import views

urlpatterns = [
    url(r'showtime',views.showtime),
    url(r'list',views.showtime_list)
]