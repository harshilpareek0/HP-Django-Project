from django.urls import include, path
from django.views.generic import TemplateView
from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView,InputExerciseView,ShowProfilePageView,CreateProfilePageView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name = 'index'),
    path('game/', views.index),
    path('accounts/', include('allauth.urls')),
    path('profile/',views.ProfileInputView.as_view(),name='profileinput'),
    path('profile/list', views.ProfileView.as_view(), name='profile'),
    path('edit_profile', UserEditView.as_view(), name = 'edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'), name = 'change_password')
    path('password/', PasswordsChangeView.as_view(template_name='change-password.html'), name = 'change_password'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('progress/', views.ProgressView.as_view(), name ='progress'),
    path('exercise/', views.InputExerciseView.as_view(), name='exerciseinput'),
    path('forum_post/', views.PostForumView.as_view(), name='forumpost'),
    path('forum/', views.ForumView.as_view(), name='forum'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]