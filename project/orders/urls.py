from django.urls import path

from .views import OrderListView, async_view

app_name = "orders"

urlpatterns = [
    path("", OrderListView.as_view(), name="list"),
    path("async", async_view, name="async_view")
]
