from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.planillas, name='planillas'),
    url(r'^registrar$', views.registrar, name='registrar'),
]