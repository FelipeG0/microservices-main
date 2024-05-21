from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^places/', views.PlaceList),
    url(r'^placecreate/$', csrf_exempt(views.PlaceCreate), name='placeCreate')
    path('places/check/<int:place_id>/', views.check_place, name='check_place'),
]
