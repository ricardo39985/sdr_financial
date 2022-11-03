from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
# Decoreator to ensure user is logged in
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


# Views


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class MyPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/change-password.html'
    success_url = '/dashboard/'


# Get form for user update
@login_required
def update_user(request):
    return render(request, 'profiles/update.html')


@login_required
def apply_user_update(request):
    profile = request.user.profile
    profile.first_name = request.POST['first_name'] if request.POST['first_name'] else profile.first_name
    profile.last_name = request.POST['last_name'] if request.POST['last_name'] else profile.last_name
    profile.bio = request.POST['bio'] if request.POST['bio'] else profile.bio
    profile.address = request.POST['address'] if request.POST['address'] else profile.address
    profile.save()
    messages.add_message(request, messages.INFO,
                         'Your info has been saved')

    return redirect('update_user')
