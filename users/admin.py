from django.contrib import admin
from django.contrib.auth import get_user_model
from users.forms import UserAdminChangeForm, UserAdminCreationForm

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'is_superuser', 'is_active', 'is_blocked')
    list_filter = ('is_active', 'is_blocked')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_active', 'is_blocked', )}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_superuser', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)