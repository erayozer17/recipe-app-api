from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as gt

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    # Fields to show in a user's admin detail page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (gt('Personal Info'), {'fields': ('name',)}),
        (gt('Permissions'), {'fields': ('is_active', 'is_staff',
                                        'is_superuser')}),
        (gt('Important dates'), {'fields': ('last_login',)}),
    )
    # Required fields in order to add a new user on admin's user page
    add_fieldsets = (
        (None, {
            # Classes is just a way of UI
            'classes': ('wide',),
            # password1 and password2 will appear as password and \
            # password confirmation and they will enforce password validation
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
