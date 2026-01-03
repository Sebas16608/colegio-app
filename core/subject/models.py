from django.db import models
from user.models import User
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subject")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        unique_together = ("teacher", "name")

    def __str__(self):
        return f"Subject {self.name} by {self.teacher.username}"