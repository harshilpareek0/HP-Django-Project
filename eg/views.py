from django.http import HttpResponse
from .models import Profile
from .models import Exercise
from .models import Posts
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView,DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse, reverse_lazy
from .forms import EditProfileForm, ProfilePageForm
from django.shortcuts import render, get_object_or_404
from django.template import loader
from math import floor

class CreateProfilePageView(CreateView):
    model = Profile
    #form_class = ProfilePageForm
    template_name = "create_user_profile_page.html"
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

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
    #fields = ['username','creation_date','age']

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('index')
    def get_object(self):
        return self.request.user

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    def get_success_url(self):
        return reverse('index')

class InputExerciseView(generic.CreateView):
    model = Exercise
    template_name = 'exercise.html'
    fields = ['exercise_name']

class ProgressView(generic.TemplateView):
    template_name = 'progress.html'
    def get_context_data(self, **kwargs):
        progress = (Exercise.objects.count() % 10) * 100
        progress_percentage = progress / 10
        level = floor(Exercise.objects.count() / 10)
        context = super(ProgressView, self).get_context_data(**kwargs)
        context.update({'progress': progress, 'progress_percentage': progress_percentage, 'level':level})
        return context

class PostForumView(generic.CreateView):
    model = Posts
    template_name = 'forum_post.html'
    fields = ['post_text']

class ForumView(generic.ListView):
    context_object_name = 'posts'
    template_name = 'forum.html'
    def get_queryset(self):
        return Posts.objects.all()

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self,*args,**kwargs):
       user=Profile.objects.all() 
       context= super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
       page_user = get_object_or_404(Profile,id = self.kwargs['pk'])
       context["page_user"] = page_user
       return context