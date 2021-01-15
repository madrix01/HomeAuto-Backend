from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('io1/', csrf_exempt(views.index1)),
    path('io/', csrf_exempt(views.ioDevice)),
    path('room/add/', csrf_exempt(views.addRoomView)),
    path('room/', csrf_exempt(views.roomList)),
    path('boards/room/<int:id>', csrf_exempt(views.roomBoards)),
    path('devices/board/<int:id>', csrf_exempt(views.boardDevices)),
    path('devices/room/<int:id>', csrf_exempt(views.roomDevices))
]
