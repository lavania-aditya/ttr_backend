from django.urls import path

from apps.admins.views import AdminLoginAPIView, UploadImageAPIView

urlpatterns = [
    path("admin/login", AdminLoginAPIView.as_view(), name="admin-login"),
    path("upload-image", UploadImageAPIView.as_view(), name="upload-image"),
]
