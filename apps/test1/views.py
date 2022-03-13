from apps.test1.forms import OrderForm
from .models import Customer, Order, Product
from django.shortcuts import redirect, render
from django.views import View
from .filter import orderFilter

class IndexView(View):

    def get(self, request, *args, **kwargs):
        filter = orderFilter()
        orders = Order.objects.all()
        customers = Customer.objects.all()
        total_customer = customers.count()
        myfiler = orderFilter(request.GET, queryset=orders)
        orders = myfiler.qs
        context = {'orders':orders, 'customers':customers,'filter':filter}


        return render(request, 'test1.html', context)

class ProductView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test1/product_all.html')

class OrderCreateView(View):
    def get(self, request, *args, **kwargs):
        form = OrderForm()
        return render(request, 'test1/order_create.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'test1.html', {'form':form})

class OrderUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)
        return render(request, 'test1/order_create.html', {'form':form})
    def post(self, request, pk, *args, **kwargs):
        order = Order.objects.get(id=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'test1.html', {'form':form})





class OrderDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        order = Order.objects.get(id=pk)
        return render(request, 'test1/order_delete.html', {'order':order})
    def post(self, request, pk, *args, **kwargs):
        order = Order.objects.get(id=pk)
        order.delete()
        return redirect('index')
        # return render(request, 'test1.html', )
        