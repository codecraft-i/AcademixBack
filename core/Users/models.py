# apps/admissions/models.py
from django.db import models

class StudyInquiry(models.Model):
    first_name              = models.CharField(max_length=50)
    last_name               = models.CharField(max_length=50)
    email                   = models.EmailField()
    phone_number            = models.CharField(max_length=20)
    telegram_nickname       = models.CharField(max_length=32, blank=True)
    wanted_country_of_study = models.CharField(max_length=64)
    study_program           = models.CharField(max_length=128)
    planning_money          = models.DecimalField(max_digits=12, decimal_places=2)
    text_message            = models.TextField(blank=True)

    submitted_at            = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.wanted_country_of_study}"
