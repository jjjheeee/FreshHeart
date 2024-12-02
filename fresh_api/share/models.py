from django.db import models

class TimeModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
class Emotions(models.Model):
    emotion = models.TextField()
    emotion_color = models.TextField()
    emotion_sticker = models.TextField()