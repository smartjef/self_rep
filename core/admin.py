from django.contrib import admin
from .models import Contact, Service, Team, Profile
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'image', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'slug', 'description']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'image', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['user__username', 'user__email', 'role']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created']
    list_filter = ['created']
    search_fields = ['name', 'email', 'subject', 'message']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'user_type','field', 'skype', 'twitter', 'instagram',  'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['user__username', 'user__email', 'gender', 'field', 'user_type',]