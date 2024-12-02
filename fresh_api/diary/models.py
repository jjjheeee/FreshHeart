from django.db import models
from share.models import TimeModel

# Create your models here.
class Diary(TimeModel):
    user_id = models.ForeignKey(
        'user.Users',
        on_delete=models.SET_NULL,
        null=True
    )
    emotion_id = models.ForeignKey(
        'share.Emotions',
        on_delete=models.SET_NULL,
        null=True
    )
    is_secreat = models.BooleanField(
        
    )
    message = models.JSONField(
        # { user : [ ], bot : [ ] }
        default=dict
    )
    is_active = models.BooleanField(
        default = True
    )
    cheer_up = models.IntegerField(
        default=0
    )
    like_count = models.IntegerField(
        default=0
    )
    message_summary = models.JSONField(
        # { user : "", bot : "", emotion : "" }
        default=dict
    )