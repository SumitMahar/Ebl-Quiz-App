from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages


from .forms import CustomUserCreationForm


def register(request):
    ''' 
        Registers and logs the new user in
    '''
    if request.method == 'POST':
        # Process filled form
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            authenticated_user = authenticate(request, username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            messages.success(request, f'Account created for {username} ')
            return HttpResponseRedirect(reverse('quizes:quiz_home'))
    
    else:
        #Display blank registration form
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html' , context)


def logout_view(request):
    ''' Logs out the current user '''
    logout(request)
    return HttpResponseRedirect(reverse('quizes:quiz_home'))
