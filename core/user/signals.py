from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        send_mail(
            subject = "Colegio Mixto Nuestra Señora del Pilar",
            message = f"Hola {instance.first_name} bienvenido a la plataforma oficial del Colegio Mixto 'Nuestra Señora del Pilar'",
            from_email = None,
            recipient_list = [instance.email],
            fail_silently = True
        )