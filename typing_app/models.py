# typing_app/models.py
from django.db import models

class TypingData(models.Model):
    sleep_time = models.FloatField()
    count = models.IntegerField()
    text = models.CharField(max_length=255)
