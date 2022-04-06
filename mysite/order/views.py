

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import ContainerType, ContainerSpec
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import CreateOrder


class OrderListView(ListView):
    model = ContainerSpec
    template_name = 'order/index.html'
    paginate_by=10
    def get_queryset(self):
        return ContainerSpec.objects.all()

def order_list(request):
    order = ContainerSpec.objects.all()
    paginator = Paginator(order, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
    }
    return render(request, 'order/index.html', context)

def order_detail(request, get_booking):
    booking = get_object_or_404(ContainerSpec, booking_no = get_booking)
    context = {
        'object': booking
    }

    return render(request, 'order/order_detail.html', context)

def create_order(request):
    order = "Create"
    form = CreateOrder(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("order:order_detail", kwargs={'get_booking': form.instance.booking_no} ))


    context = {
        'order': order,
        'form': form,
    }

    return render(request, 'order/create_order.html', context)

def update_order(request, get_booking):
    order = "Update"
    booking = get_object_or_404(ContainerSpec, booking_no = get_booking)
    form = CreateOrder(request.POST or None,
                       request.FILES or None,
                       instance=booking)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("order:order_detail", kwargs={'get_booking': form.instance.booking_no}  ))


    context = {
        'order': order,
        'form': form,
        # 'object': booking,
    }

    return render(request, 'order/create_order.html', context)

def order_delete(request, get_booking):
    booking = get_object_or_404(ContainerSpec, booking_no = get_booking)
    booking.delete()
    return redirect(reverse('order:order_list'))

class OrderDelete(DeleteView):
    template_name = 'order/delete_order.html'
    def get_success_url(self):
        return reverse_lazy("order:order_list")

    def get_object(self):
        get_booking = self.kwargs.get("get_booking")
        return get_object_or_404(ContainerSpec, booking_no=get_booking)
