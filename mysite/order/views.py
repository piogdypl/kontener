

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import ContainerType, ContainerSpec
from django.views.generic import ListView, DeleteView

from django.urls import reverse_lazy
from .forms import CreateOrder
from .filters import OrderFilter


from django.views import generic
import django_filters


class OrderDashBoard(ListView):
    model = ContainerSpec
    template_name = 'order/dashboard.html'
    limit = 5


    def get_queryset(self):
        return ContainerSpec.objects.all().order_by('date')[10:]

class OrderListView(ListView):
    model = ContainerSpec
    template_name = 'order/index.html'
    paginate_by = 10

    def get_queryset(self):
        return ContainerSpec.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = OrderFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return OrderFilter(self.request.GET, queryset=queryset).qs

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


class OrderDelete(DeleteView):
    template_name = 'order/delete_order.html'
    def get_success_url(self):
        return reverse_lazy("order:order_list")

    def get_object(self):
        get_booking = self.kwargs.get("get_booking")
        return get_object_or_404(ContainerSpec, booking_no=get_booking)

