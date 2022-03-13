from django.forms import ModelForm

from apps.test1.models import Order, Product


class ProjectForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

