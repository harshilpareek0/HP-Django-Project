from django.http import HttpResponse
from .models import Profile
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditProfileForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')


def index(request):
    return HttpResponse("Hello, world. You're at the exgame index.")


class IndexView(generic.ListView):
    template_name = 'index.html'

def profile(request):
    return HttpResponse("This is your profile.")

class ProfileView(generic.ListView):
    context_object_name = 'latest_profile_list'
    template_name = 'profile.html'
    def get_queryset(self):
        return Profile.objects.all()

class ProfileInputView(CreateView):
    model = Profile
    template_name = 'profile_input.html'
    fields = ['username','creation_date','age']

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user