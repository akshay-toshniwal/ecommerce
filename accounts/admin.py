from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



User = get_user_model()
# Register your models here.
class UserAdmin(BaseUserAdmin):

    list_display = ('id', 'name', 'email')
    list_ordering = ['-id']
    list_filter = ('shop', 'active')
    fieldsets = (
        ('Personal info', {'fields': ('name','email', 'address','dob')}),
        ('Permissions', {'fields': ('shop', 'active', 'admin',
          )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email')}
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
