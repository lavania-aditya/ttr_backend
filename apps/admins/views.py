from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.admins.serializers import AdminLoginSerializer
from utils.cloudinary_upload import upload_image_to_cloudinary


class AdminLoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = AdminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UploadImageAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        if not image:
            return Response({"detail": "Image file is required"}, status=status.HTTP_400_BAD_REQUEST)

        image_url = upload_image_to_cloudinary(image)
        if not image_url:
            return Response({"detail": "Image upload failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"image_url": image_url}, status=status.HTTP_201_CREATED)
