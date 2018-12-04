from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^prueba/', prueba, name="prueba"),
    url(r'^asistencia/(?P<id>\d+)/$', asistencia, name="asistencia"),
    url(r'^list/(?P<id>\d+)/$', list_render, name="list"),
    url(r'^list2/(?P<id>\d+)/$', list_render2, name="list2"),
    url(r'^login/', login_user, name="login"),
    url(r'^logout/', logout_user, name="logout"),
    url(r'^register/', register_user, name="register"),
    url(r'^ausente/', ausente, name="ausente"),
    url(r'^undo_falta/', undo_falta, name="undo_falta"),
    url(r'^create_student/', create_student, name="create_student"),
    url(r'^main/', main, name="main"),
    url(r'^manage/', manage, name="manage"),
    url(r'^preceptor_list/', preceptor_list, name="preceptor_list"),
    url(r'^update_preceptor/', update_preceptor, name="update_preceptor"),
    url(r'^student_list/', student_list, name="student_list"),
    url(r'^update_student/', update_student, name="update_student"),
    url(r'^late_arrival/', late_arrival, name="late_arrival"),
    url(r'^undo_latearrival/', undo_latearrival, name="undo_latearrival"),
    url(r'^late/(?P<id>\d+)/$', late_render, name="late"),
    url(r'^early_retirement/', early_retirement, name="early_retirement"),
    url(r'^undo_retirement/', undo_retirement, name="undo_retirement"),
    url(r'^early/(?P<id>\d+)/$', early_render, name="early"),
    url(r'^justify/', justify, name="justify"),
    url(r'^upload/(?P<id>\d+)/$', upload, name="upload"),
    url(r'^undo_justify/', undo_justify, name="undo_justify"),
    url(r'^justification/(?P<id>\d+)/$', justification_render, name="justification"),
    url(r'^export/xls/$', excel , name='excel'),
    url(r'^comedor/$', comedor , name='comedor'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)