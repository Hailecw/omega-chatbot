from django.shortcuts import render
from django.urls import reverse_lazy
from .models import MessagesModel,TabModel
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView


@login_required(login_url=reverse_lazy('login'))
def HomePage(request):
    history = TabModel.objects.filter(user=request.user)
    current = history.last()
    if not current:
        current = TabModel.objects.create(user=request.user)
    msg = current.chats.all()
    return render(request,"base/home.html",{'msg':msg,'history':history[::-1],'h':'<h1>Hello World</h1>'})


class TabDetailView(DetailView):
    model = TabModel
    template_name = "base/home_detail.html"
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        pk = self.object.pk
        print(pk)
        current = TabModel.objects.get(pk=pk)
        context['msg'] = current.chats.all()
        history = TabModel.objects.filter(user=self.request.user)
        context['history'] = history
        return context
    
