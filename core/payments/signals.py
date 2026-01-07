# payments/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment

@receiver(post_save, sender=Payment)
def update_student_solvent(sender, instance, **kwargs):
    if instance.status == "APPROVED":
        instance.student.update_solvent_status()
