from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from .models import Order, Product
from .tasks import sample_task


class OrderListView(ListView):
    model = Order


def async_view(request):
    sample_task.delay()
    return HttpResponse("test async")
