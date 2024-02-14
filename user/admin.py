from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile


class Admin(UserAdmin):
    filter_horizontal = ()
    list_filter = ('is_active',)
    fieldsets = ()
    ordering = ['email']
    list_display = ('phone', 'fullName')


class PAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(User, Admin)

admin.site.register(Profile, PAdmin)
