# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = CustomUser
#     list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
#     add_fieldsets = UserAdmin.add_fieldsets + (
#     (None, {'fields': ('email', 'first_name', 'last_name', 'display_name', 'date_of_birth', 'address1', 'address2', 'zip_code', 'city', 'additional_information',)}),
# )
# fieldsets = UserAdmin.fieldsets + (
#     (None, {'fields': ('display_name', 'date_of_birth', 'address1', 'address2', 'zip_code', 'city', 'additional_information')}),
# )


# admin.site.register(CustomUser, CustomUserAdmin)

# from django.contrib import admin

# from .models import Profile

# admin.site.register(Profile)

# # Register your models here.

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# from .models import Profile

# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)