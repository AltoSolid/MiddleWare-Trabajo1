from django.db import models

# Create your models here.

class Room(models.Model):
    roomName = models.CharField(max_length=20, unique=True)
    roomTopic = models.CharField(max_length=50)

class Message(models.Model):
    messContent = models.CharField(max_length=500)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)