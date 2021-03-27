from django.urls import include, path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('game/', views.index),
    path('accounts/', include('allauth.urls')),
    path('profile/',views.ProfileInputView.as_view(),name='profileinput'),
    path('profile/list', views.ProfileView.as_view(), name='profile'),
]