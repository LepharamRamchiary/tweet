from django import template
from django import forms

register = template.Library()

@register.filter(name="add_class")
def add_class(value, css_class):
    return value.as_widget(attrs={"class": css_class})



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control'})
    )