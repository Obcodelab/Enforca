from django.db import models
from apps.users.models import User
import uuid


# Create your models here.
class CalendarEvent(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    video_link = models.URLField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_events"
    )
    candidate = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="candidate_events"
    )

    def __str__(self):
        return f"{self.title} - {self.candidate}"
