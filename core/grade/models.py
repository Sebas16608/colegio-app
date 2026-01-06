from django.db import models
from submission.models import Submission
# Create your models here.
class Grade(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="grades")
    grade = models.PositiveIntegerField()
    feedback = models.TextField(blank=True, null=True)
    graded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

    def __str__(self):
        return f"Grade {self.grade} for {self.submission.assignment.title} by {self.submission.student.username}"
