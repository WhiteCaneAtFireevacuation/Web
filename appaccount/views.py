from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from appaccount.models import HelloWorld

# Create your views here.
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from appaccount.forms import AccountUserCreationForm, AccountUserUpdateForm


def hello_world(request):
    #return HttpResponse('히히')
    
    if request.method=="POST":
        #요청을 받은 메소드가 post일 경우 아래 html을 리턴한다.
        temp=request.POST.get('hello_world_input')
    
        new_hello_world=HelloWorld()
        new_hello_world.text=temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('appaccount:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request,'appaccount/sub_page.html',context={'hello_world_list': hello_world_list})


        
class AccountCreateView(CreateView):
    
    model = User
    form_class = AccountUserCreationForm
    success_url = reverse_lazy('appaccount:hello_world')
    template_name = 'appaccount/account_user.html'


class AccountUserDetailView(DetailView):
    model = User
    context_object_name = 'user_name'
    form_class = UserCreationForm
    template_name = 'appaccount/account_user_detail.html'
    
class AccountUserUpdateView(UpdateView):
    model = User
    context_object_name = 'user_name'
    form_class = AccountUserUpdateForm
    success_url = reverse_lazy('appaccount:hello_world')
    template_name = 'appaccount/account_user_update.html'
    
class AccountUserDeleteView(DeleteView):
    model = User
    context_object_name = 'user_name'
    success_url = reverse_lazy('appaccount:login')
    template_name = 'appaccount/account_user_delete.html'
 
