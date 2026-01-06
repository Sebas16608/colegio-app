from django.db import models
from django.core.exceptions import ValidationError
from subject.models import Subject
# Create your models here.
class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="assignment")
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

    def __str__(self):
        return f"Tarea {self.id} {self.title} de {self.subject.name}"

    def submissions(self):
        return self.submission_set.all()
    
    def clean(self):
        if self.due_date < self.created_at:
            raise ValidationError("La fecha de creacion no puede ser anterior a la fecha de entrega")

