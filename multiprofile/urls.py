"""multiprofile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ngo.views import choice, ngo, donor, ad_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ngo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', choice.SignUpView.as_view(), name='signup'),
    path('accounts/signup/ngo/', ngo.NGOSignUpView.as_view(), name='ngo_signup'),
    path('accounts/signup/donor/', donor.DonorSignUpView.as_view(), name='donor_signup'),
    path('accounts/signup/admin/', ad_user.AdminSignUpView.as_view(), name='admin_signup'),
]
