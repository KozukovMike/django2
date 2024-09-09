from django import forms


class RegisterForm(forms.Form):
    email = forms.CharField(label='Email', max_length=50)
    phone = forms.CharField(label='Телефон', max_length=13)
    name = forms.CharField(label='Имя', max_length=30)
