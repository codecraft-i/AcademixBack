from django.db import models

# Create your models here.

from django.db import models

class Event(models.Model):
    class Status(models.TextChoices):
        PLANNED = "PLANNED", "Rejalashtirilgan"
        COMPLETED = "COMPLETED", "Tugagan"
    image = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=200)
    date = models.DateField()
    time_range = models.CharField(                # Masalan: "14:00 – 15:00"
        max_length=50,
        help_text="Vaqt oraliği, masalan: 14:00 – 15:00",
    )
    venue = models.CharField(                     # Joy nomi (masalan, zal)
        max_length=200,
        help_text="Tadbir o‘tkaziladigan joy nomi",
    )
    location = models.CharField(                  # Manzil / shahar
        max_length=200,
        blank=True,
        help_text="Manzil (ixtiyoriy)",
    )
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PLANNED,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-time_range"]

    def __str__(self):
        return f"{self.title} ({self.date})"
