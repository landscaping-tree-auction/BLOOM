from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'seller_status')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'seller_status')}
        ),
    )
    list_display = ('email', 'is_staff', 'is_active', 'seller_status')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'seller_status')
    search_fields = ('email',)
    ordering = ('email',)
