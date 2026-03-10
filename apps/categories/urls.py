from django.urls import path

from apps.categories.views import CategoryViewSet


category_list = CategoryViewSet.as_view({"get": "list", "post": "create"})
category_delete = CategoryViewSet.as_view({"delete": "destroy"})

urlpatterns = [
    path("categories", category_list, name="categories-list-create"),
    path("categories/<int:pk>", category_delete, name="categories-delete"),
]
