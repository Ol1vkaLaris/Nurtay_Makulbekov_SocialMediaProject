from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Личные данные', {'fields' : ('username', 'first_name', 'last_name', 'phone_number')}), 
        ('Данные для авторизации', {'fields' : ('email', 'password')}), 
        ('Доступ', {'fields' : ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}), 
        ('Доп. инфо', {'fields' : ('last_login', 'date_joined')}), 
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide'),
            'fields' : ('username', 'first_name', 'last_name', 'email', 'usable_password', 'password1', 'password2')
        },),
    )
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)
    
admin.site.register(User, CustomUserAdmin)