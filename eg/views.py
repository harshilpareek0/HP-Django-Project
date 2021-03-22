from django.views import generic
from django.contrib.auth.models import User 
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, HttpResponseRedirect

#from .models import Profile


def index(request):
    return HttpResponse("Hello, world. You're at the exgame index.")


class IndexView(generic.ListView):
    template_name = 'index.html'


# def creationTest(*user_id):
#     #model = Profile
#     return render('eg/account_creation.html')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('Profile')

    def get_object(self):
        return self.request.user

class Profile(generic.DetailView):
    template_name = 'profile.html'
    queryset = User.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User,username=id_)
        return user


# def accountCreation(request):
#     if request.method == 'POST':



# def see_request(request):
#     text = f"""
#         Some attributes of the HttpRequest object:

#         scheme: {request.scheme}
#         path:   {request.path}
#         method: {request.method}
#         GET:    {request.GET}
#         user:   {request.user}
#     """

#     return HttpResponse(text, content_type="text/plain")