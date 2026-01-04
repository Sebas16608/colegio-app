from django.db import models
from user.models import User
from subject.models import Subject
# Create your models here.
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollment")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    creatred_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return f"{self.student} ({self.subject})"