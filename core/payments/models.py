# payments/models.py
from django.db import models
from user.models import User

class Payment(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Ejemplo: "2026-01"
    month = models.CharField(max_length=7)

    reference_number = models.CharField(max_length=100, unique=True)

    receipt = models.FileField(upload_to="payments/receipts/")

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    validated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="validated_payments"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.student.username} - {self.month} - {self.status}"
