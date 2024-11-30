from django.shortcuts import render
from django.urls import reverse_lazy
from .models import MessagesModel,TabModel
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('login'))
def HomePage(request):
    if request.method == 'POST':
        print("insie post")
        TabModel.objects.create(user=request.user)
    history = TabModel.objects.filter(user=request.user)
    current = history.last()
    if not current:
        current = TabModel.objects.create(user=request.user)
    msg = current.chats.all()
    return render(request,"base/home.html",{'msg':msg,'history':history[::-1]})



    
