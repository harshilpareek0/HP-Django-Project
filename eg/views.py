from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from .models import Exercise
from .models import Posts
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse, reverse_lazy
from .forms import EditProfileForm, PostForm, ReplyForm, ExerciseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.template import loader
from math import floor

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

def InputExerciseView(request):
    form = ExerciseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.exerciser_name = request.user
            obj.save()
            form = ExerciseForm()
            return redirect('/progress/' + str(request.user.id) + '/')
    return render(request, 'exercise.html', {'form': form})

class ProgressView(generic.TemplateView):
    template_name = 'progress.html'
    def get_context_data(self, **kwargs):
        progress = (Exercise.objects.filter(exerciser_name=self.kwargs['userid']).count() % 10) * 100
        progress_percentage = progress / 10
        level = floor(Exercise.objects.filter(exerciser_name=self.kwargs['userid']).count() / 10)
        context = super(ProgressView, self).get_context_data(**kwargs)
        context.update({'progress': progress, 'progress_percentage': progress_percentage, 'level':level})
        return context

def PostForumView(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post_maker = request.user
            obj.post_number = Posts.objects.count() + 1
            obj.save()
            form = PostForm()
            return redirect('/forum/')
    return render(request, 'forum_post.html', {'form': form})

def ReplyView(request, pn):
    form = ReplyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.reply_maker = request.user
            obj.post = Posts.objects.filter(post_number=pn)[0]
            request.POST.get('reply_text')
            obj.save()
            form = ReplyForm()
            return redirect('/forum/')
    return render(request, 'forum_post.html', {'form': form})

class ForumView(generic.ListView):
    context_object_name = 'posts'
    template_name = 'forum.html'
    def get_queryset(self):
        return Posts.objects.all()

def LikeView(request, pn):
    Posts.objects.filter(post_number=pn).update(likes=Posts.objects.filter(post_number=pn)[0].likes + 1)
    return HttpResponseRedirect(reverse('forum'))

class ForumProfileView(generic.ListView):
    context_object_name = 'profile_info'
    template_name = 'view_profile.html'
    def get_queryset(self):
        return Profile.objects.filter(user=self.kwargs['userid'])
