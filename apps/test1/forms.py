from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from apps.test1.models import Order, Product
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



