from django.db import models
from django.utils import timezone

class Event(models.Model):
    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_time = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
