
# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sigin/" , views.sigin , name="sigin"),
    path("<str:room_name>/<str:name>", views.room, name="room"),
     
]