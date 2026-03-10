from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.admins.models import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    model = AdminUser
    ordering = ("-created_at",)
    list_display = ("email", "role", "is_staff", "is_active", "created_at")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("role", "is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "created_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "role", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    readonly_fields = ("created_at", "last_login")
