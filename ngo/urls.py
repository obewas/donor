
from django.urls import path
from ngo.views import ngo, donor

urlpatterns = [

path('', ngo.NGOListView.as_view(), name='home'),
path('ngo_create', ngo.NGOCreateView.as_view(), name='ngo_create'),
path('donor_create', donor.DonorCreateView.as_view(), name='donor_create'),
path('donorlist', donor.DonorListView.as_view(), name='donor_list'),
path('profile/', ngo.ngoProfile, name='ngo-profile'),
path('donor_profile', donor.donorProfile, name='donor-profile'),
]

