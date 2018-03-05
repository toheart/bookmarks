from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == "POST": #POST 请求
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse("Invalid login")
    else:                      #GET请求
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

