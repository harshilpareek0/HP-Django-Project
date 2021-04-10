from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from .models import Exercise
from .models import Posts
# from .models import GymMap
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse, reverse_lazy
from .forms import EditProfileForm, PostForm, ReplyForm
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from math import floor

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

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
    #form_class = UserProfileForm
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
        progress = (Exercise.objects.filter(exerciser_name=Profile.user.username).count() % 10) * 100
        progress_percentage = progress / 10
        level = floor(Exercise.objects.count() / 10)
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

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

# class LocationView(generic.UpdateView):
#     form_class = UserProfileForm
#     template_name = 'location_test.html'
#     success_url = reverse_lazy('index')
#     def get_object(self):
#         return self.request.user


# class GymMapView(generic.CreateView):
#     model = GymMap
#     template_name = 'location_test.html'
#     fields = ['location']

def music(request): 
    boogie_uri = 'spotify:artist:31W5EY0aAly4Qieq6OFu6I'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = '7bf326e10aca4f7284dc44c36817c6e3', client_secret = 'ff31284598a940cf999ccf42fdbf4d16'))
    #results = spotify.album(album_uri)
    results = spotify.artist_top_tracks(boogie_uri)
    songs_results = results['tracks'][:20]
    return render(request,'our-music-choice.html',{"results":songs_results})
def LikeView(request, pn):
    Posts.objects.filter(post_number=pn).update(likes= Posts.objects.filter(post_number=pn)[0].likes + 1)
    return HttpResponseRedirect(reverse('forum'))
