from django import forms
from django.contrib.auth.models import User

class AccountFrom(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100,min_length=8,widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100,min_length=8,widget=forms.PasswordInput())
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            return forms.ValidationError("username already exist!")
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email or '.com' not in email:
            return forms.ValidationError("your email is not in right format")
        return email
    def clean_password(self):
        password = self.cleaned_data['password']
        print(self.cleaned_data)
        password2 = self.cleaned_data['password2']
        if password!=password2:
            return forms.ValidationError("passwords are not similar")
        return password


