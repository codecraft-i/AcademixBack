from django.urls import path
from .views import StudyInquiryCreateView, StudyInquiryListView

urlpatterns = [
    path("inquiries/", StudyInquiryCreateView.as_view(), name="inquiry-create"),
    path("inquiries/list/", StudyInquiryListView.as_view(), name="inquiry-list"),
]