from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from ngo.decorators import unauthenticated_user
from ngo.forms import NGOSignUpForm,UserUpdateForm, NGOProfileUpdateForm, DonorProfileUpdateForm
from ngo.models import User, NGO, Donor, NGOProfile
from django.contrib import messages
# Create your views here.


class NGOSignUpView(CreateView):
    model = User
    form_class = NGOSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        is_ngo = True
        kwargs['user_type'] = 'ngo'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('ngo-profile')


class NGOListView(ListView):
    model = NGO
    template_name = 'ngolist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
  
        return context


class NGOCreateView(CreateView):
    model = NGO
    template_name = 'ngocreate.html'
    fields = '__all__'
    success_url = '/'


def ngoProfile(request):
    NGOProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = NGOProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.ngoprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('ngo-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = NGOProfileUpdateForm(instance=request.user.ngoprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'ngo-profile.html', context)




