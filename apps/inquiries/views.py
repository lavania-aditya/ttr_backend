from rest_framework import generics

from apps.inquiries.models import Inquiry
from apps.inquiries.serializers import InquirySerializer


class InquiryCreateAPIView(generics.CreateAPIView):
    queryset = Inquiry.objects.select_related("product").all()
    serializer_class = InquirySerializer
