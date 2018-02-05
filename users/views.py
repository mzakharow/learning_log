from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """end session app"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    if request.method != 'POST':
        #Display blank registration form
        form = UserCreationForm()
    else:
        # обработка заполненой формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # entrance end redirect to home page
            authenticated_user = authenticate(username=new_user, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

