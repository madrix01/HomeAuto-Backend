from django.db import models

class Rooms(models.Model):
    roomName = models.CharField(max_length=20)
    floor = models.CharField(max_length=5)
    
    def __str__(self):
        return self.roomName


class Board(models.Model):
    boardName = models.CharField(max_length=50)
    boardIp = models.CharField(max_length=20)
    roomId = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def __str__(self):
        return self.boardName

class Device(models.Model):
    deviceName = models.CharField(max_length=50)
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.deviceName
