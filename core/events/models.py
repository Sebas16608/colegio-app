from django.db import models
from user.models import User
# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name=("events"))
    
    class Meta:
        ordering = ["start_date"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title