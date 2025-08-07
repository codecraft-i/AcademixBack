# apps/admissions/views.py
from rest_framework import generics, permissions
from .models import StudyInquiry
from .serializers import StudyInquirySerializer

class StudyInquiryCreateView(generics.CreateAPIView):
    """
    Faqat POST (create) uchun endpoint:
    /api/admissions/inquiries/
    """
    queryset         = StudyInquiry.objects.all()
    serializer_class = StudyInquirySerializer
    permission_classes = [permissions.AllowAny]   # yoki JWT bo'lsa o'zgartiring

class StudyInquiryListView(generics.ListAPIView):
    queryset         = StudyInquiry.objects.all().order_by("-submitted_at")
    serializer_class = StudyInquirySerializer
    permission_classes = [permissions.IsAuthenticated]   # faqat adminlar
