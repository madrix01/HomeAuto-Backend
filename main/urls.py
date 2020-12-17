from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('io/', csrf_exempt(views.index)),
    path('io1/', csrf_exempt(views.index1)),
    path('room/add/', csrf_exempt(views.addRoomView)),
    path('room/', csrf_exempt(views.roomList))
]
