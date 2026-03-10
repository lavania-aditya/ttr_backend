from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

AdminUser = get_user_model()


class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = AdminUser.objects.filter(email__iexact=email, is_active=True).first()

        if not user or not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "admin": {
                "id": user.id,
                "email": user.email,
                "role": user.role,
                "created_at": user.created_at,
            },
        }
