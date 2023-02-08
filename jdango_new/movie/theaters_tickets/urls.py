from django.urls import re_path as url

from movie.theaters_tickets import views

urlpatterns = [
    url(r'theater_ticket',views.theater_ticket),
    url(r'list',views.theater_ticket_list)
]