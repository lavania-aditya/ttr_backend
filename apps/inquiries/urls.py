from django.urls import path

from apps.inquiries.views import InquiryCreateAPIView

urlpatterns = [
    path("inquiries", InquiryCreateAPIView.as_view(), name="inquiry-create"),
]
