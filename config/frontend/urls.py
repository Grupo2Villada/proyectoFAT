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
    url(r'^ausente/', ausente, name="ausente"),
    url(r'^create_student/', create_student, name="create_student"),
    url(r'^main/', main, name="main"),
    url(r'^manage/', manage, name="manage"),
    url(r'^preceptor_list/', preceptor_list, name="preceptor_list"),
    url(r'^update_preceptor/', update_preceptor, name="update_preceptor"),
    url(r'^student_list/', student_list, name="student_list"),
    url(r'^update_student/', update_student, name="update_student"),
    url(r'^late_arrival/', late_arrival, name="late_arrival"),
    url(r'^late/(?P<id>\d+)/$', late_render, name="late"),
    url(r'^early_retirement/', early_retirement, name="early_retirement"),
    url(r'^early/(?P<id>\d+)/$', early_render, name="early"),
    url(r'^justify/', justify, name="justify"),
    url(r'^justification/(?P<id>\d+)/$', justification_render, name="justification"),
    url(r'^export/xls/$', excel, name='excel'),
]
