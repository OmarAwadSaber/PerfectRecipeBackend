from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Adjust if your model is named differently
from django.forms import TextInput, Textarea
from django import forms

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        widgets = {
            'email': TextInput(attrs={'size': '30'}),
        }

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm

    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
