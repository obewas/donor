from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from ngo.models import User, Donor, DonorProfile
from ngo.forms import DonorSignUpForm, UserUpdateForm, DonorProfileUpdateForm
from django.contrib import messages

# Create your views here.

class DonorSignUpView(CreateView):
    model = User
    form_class = DonorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'donor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('donor-profile')

class DonorCreateView(CreateView):
    model = Donor
    template_name = 'donorcreate.html'
    fields = '__all__'
    success_url = '/'

class DonorListView(ListView):
    model = Donor
    template_name = 'donorlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def donorProfile(request):
    DonorProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = DonorProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.donorprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = DonorProfileUpdateForm(instance=request.user.donorprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'donor-profile.html', context)
