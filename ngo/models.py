from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

################### NGO ################################################
class NGOProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            NGOProfile.objects.get_or_create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.ngoprofile.save()


class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    need = models.TextField()
    amount = models.IntegerField()
    posted = models.DateTimeField(auto_now_add=True)



    def __str__(self):
    	return self.name
########################### Donor ####################################################    

class DonorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)
    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            DonorProfile.objects.get_or_create(user=instance)
    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.donorprofile.save()

class Donor(models.Model):
	name = models.CharField(max_length=100, null=True)
	amount = models.IntegerField()

######################################### Admin #############################################


class AdminProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            AdminProfile.objects.get_or_create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.adminprofile.save()


class Admin(models.Model):
    name = models.CharField(max_length=100, null=True)

