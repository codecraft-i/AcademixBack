# apps/admissions/serializers.py
from rest_framework import serializers
from .models import StudyInquiry

class StudyInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model  = StudyInquiry
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "telegram_nickname",
            "wanted_country_of_study",
            "study_program",
            "planning_money",
            "text_message",
            "submitted_at",
        ]
        read_only_fields = ("id", "submitted_at")
