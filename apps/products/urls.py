from django.urls import path

from apps.products.views import ProductViewSet


product_list = ProductViewSet.as_view({"get": "list", "post": "create"})
product_detail = ProductViewSet.as_view({"get": "retrieve"})
product_mutation = ProductViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})

urlpatterns = [
    path("products", product_list, name="products-list-create"),
    path("products/<slug:slug>", product_detail, name="products-detail"),
    path("products/<int:pk>", product_mutation, name="products-mutate"),
]
