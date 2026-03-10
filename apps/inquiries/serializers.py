from rest_framework import serializers

from apps.inquiries.models import Inquiry


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ["id", "name", "phone", "message", "product", "created_at"]
        read_only_fields = ["id", "created_at"]
