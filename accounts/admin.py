from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class UserAdmin(BaseUserAdmin):

    list_display = ('id', 'name', 'username', 'email')
    list_ordering = ['-id']
    list_filter = ('shop', 'is_active', 'admin')
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields': ('name', 'username', 'address','gender')}),
        ('Permissions', {'fields': ('shop', 'is_active', 'admin',
          )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username')}
         ),
    )

    search_fields = ('email', 'name')
    ordering = ('email', 'name', 'id')
    filter_horizontal = ()

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin)