from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^prueba/', prueba, name="prueba"),
    url(r'^list/', list_render, name="list"),
    url(r'^login/', login_user, name="login"),
    url(r'^logout/', logout_user, name="logout"),
    url(r'^register/', register_user, name="register"),

]
