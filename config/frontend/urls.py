from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', main, name="main"),
    url(r'^prueba/', prueba, name="prueba"),
    url(r'^list/(?P<id>\d+)/$', list_render, name="list"),
    url(r'^login/', login_user, name="login"),
    url(r'^logout/', logout_user, name="logout"),
    url(r'^register/', register_user, name="register"),
    url(r'^ausente/', ausente, name="ausente"),
    url(r'^index/', index, name="index"),
    url(r'^create_student/', create_student, name="create_student")

]
