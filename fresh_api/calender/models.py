from django.db import models
from share.models import TimeModel
# Create your models here.
class Calender(TimeModel):
    user_id = models.ForeignKey(
        'user.Users',
        on_delete=models.CASCADE
    )
    diary_id = models.ForeignKey(
        'diary.Diary',
        on_delete=models.CASCADE
    )
    emotion_id = models.ForeignKey(
        'share.Emotions',
        on_delete=models.CASCADE
    )