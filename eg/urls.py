from django.urls import path


from . import views
from .views import UserEditView
from .views import Profile

app_name = 'exgame'
user_id = '<user_id>'
urlpatterns = [
    path('', views.index, name='index'),
    #account creation
    path('edit_profile/',UserEditView.as_view(), name = 'edit_profile'),
    #already created account
    path('profile/', Profile.as_view(), name = 'profile')
]