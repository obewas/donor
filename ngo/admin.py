from django.contrib import admin
from .models import NGO, Donor
from django.contrib.auth.admin import UserAdmin
from .models import User, NGOProfile
# Register your models here.




admin.site.register(User, UserAdmin)
admin.site.register(NGO)
admin.site.register(Donor)
admin.site.register(NGOProfile)