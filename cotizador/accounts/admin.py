"""Admin."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """User Admin.

    Attributes:
        add_fieldsets (TYPE): Description
        fieldsets (TYPE): Description
        filter_horizontal (tuple): Description
        list_display (TYPE): Description
        list_filter (tuple): Description
        ordering (tuple): Description
        search_fields (tuple): Description
    """

    list_display = (
        'email', 'user_type', 'first_name',
        'last_name', 'is_superuser')
    list_filter = ('user_type', )
    fieldsets = (
        (None, {
            'fields': (
                'email', 'user_type', 'password',
                'first_name', 'last_name', 'is_active',
            )
        }),
        ('Permissions', {'fields': ('groups', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_type', 'email', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups',)
