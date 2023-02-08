from django.urls import re_path as url

from nlp.naver_movie import views

urlpatterns = [
    url(r'review',views.moviereview_views)
]