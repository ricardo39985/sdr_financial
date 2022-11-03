from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = 
        fields = ['first_name', 'last_name', 'email',]