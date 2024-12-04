from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import AccountFrom
from django.urls import reverse_lazy


class LoginPage(LoginView):
    form_class = AuthenticationForm
    template_name = 'user_auth/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'user_auth/signup.html'
    form_class = AccountFrom
    success_url = reverse_lazy("home")
    def post(self, request, *args, **kwargs):
        form = AccountFrom(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
                )
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

        
