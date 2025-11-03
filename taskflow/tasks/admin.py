from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task, Comment



admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_active', 'is_staff']
    list_filter = ['role', 'is_active', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('phone_number', 'role', 'bio', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets +(
        (None, {
            'classes': ('wide'),
            'fields' :( 'username', 'password1', 'password2', 'email', 'is_staff', 'is_active')
        })
    )
    search_fields = ('username', 'email')
    ordering = ('username',)