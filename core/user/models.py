from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
        ("ADMIN", "Admin")
    ]
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default="STUDENT")
    is_solvent = models.BooleanField(default=False)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
    
    def update_solvent_status(self):
        last_payment = self.payments.filter(
            status="APPROVED"
        ).order_by("-created_at").first()

        if not last_payment:
            self.is_solvent = False
        else:
            self.is_solvent = timezone.now() - last_payment.created_at <= timedelta(days=30)

        self.save(update_fields=["is_solvent"])