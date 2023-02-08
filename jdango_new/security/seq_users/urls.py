from django.urls import re_path as url

from security.seq_users import views

urlpatterns = [

    url(r'seq-login',views.login_seq),
    url(r'sequser',views.sequser),
    url(r'list$',views.sequser_list),
    url(r'listname',views.list_by_name),
    url(r'listjob',views.list_by_name),
]
