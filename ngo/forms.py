from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, NGOProfile, DonorProfile, AdminProfile
from django import forms

class NGOSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ngo = True
        user.save()
        return user


class DonorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_donor = True
        if commit:
            user.save()
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


class NGOProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= NGOProfile
        fields=['profile_image','bio']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
class DonorProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=DonorProfile
        fields=['profile_image','bio']


class AdminProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=AdminProfile
        fields=['profile_image','bio']