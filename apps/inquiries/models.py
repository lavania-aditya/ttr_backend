from django.db import models

from apps.products.models import Product


class Inquiry(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    message = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inquiries")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Inquiry by {self.name}"
