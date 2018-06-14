from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^prueba/', prueba, name="prueba"),
    url(r'^list/(?P<id>\d+)/$', list_render, name="list"),
    url(r'^login/', login_user, name="login"),
    url(r'^logout/', logout_user, name="logout"),
    url(r'^register/', register_user, name="register"),
    url(r'^create_year/', create_year, name="create_year"),
    url(r'^ausente/', ausente, name="ausente"),
    url(r'^create_student/', create_student, name="create_student"),
    url(r'^main/', main, name="main"),
    url(r'^manage/', manage, name="manage"),
    url(r'^update_preceptor/', update_preceptor, name="update_preceptor"),
    url(r'^update/', update, name="update"),

]
