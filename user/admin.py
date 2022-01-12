from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

# Register your models here.
from user.models import User


class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'package', 'date_joined')  # Contain only fields in your `custom-user-model`
    list_filter = ()  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    search_fields = ()  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ()  # Contain only fields in your `custom-user-model` intended to ordering
    filter_horizontal = ()  # Leave it empty. You have neither `groups` or `user_permissions`
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Other', {'fields': ('package',)}),
    )


admin.site.register(User, UserAdmin)

