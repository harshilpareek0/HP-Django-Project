from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Posts, Replies, Exercise, Profile
from django import forms
from eg.models import Profile

YEARS = [x for x in range(1930,2021)]

class ProfilePageForm(forms.ModelForm):
        class Meta:
                model = Profile
                fields = ('bio', 'profile_pic', 'date_of_birth' )
                widgets = {
                        'bio': forms.Textarea(attrs={'class': 'form-control'}),
                        #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
                        'date_of_birth': forms.SelectDateWidget(years = YEARS)
                }

class EditProfilePageForm(UserChangeForm):
    #bio = forms.Text(attrs={'class': 'form-control'})
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.FileField()
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years = YEARS))
    password = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'date_of_birth', 'password' )


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget = forms.HiddenInput(), required = False)
    #last_login = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #gender = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password')

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post_text']

        widgets = {
            'post_text': forms.Textarea(attrs={'class': 'form-control'})
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Replies
        fields = ['reply_text']
        
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_name']

        widgets = {'exercise_name': forms.TextInput(attrs={'class': 'form-control'})}
