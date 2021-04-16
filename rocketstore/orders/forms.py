from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Ваше имя', 'id': 'username'}),
            'phone': forms.TextInput(attrs={'class': 'userphone', 'placeholder': 'Телефон', 'id': 'userphone'}),
            'email': forms.TextInput(attrs={'class': 'useremail', 'placeholder': 'Email', 'id': 'useremail'})

        }
