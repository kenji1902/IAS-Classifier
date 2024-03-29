from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.


from .models import Authentication, voteResults
class AuthenticationInline(admin.StackedInline):
    model = Authentication
    can_delete = False
    verbose_name_plural = 'Authentication'

class UserAdmin(BaseUserAdmin):
    inlines = [AuthenticationInline]
    list_display = ['username','email', 'first_name', 'last_name', 'is_active', 'is_staff','is_authenticated','is_pending']
    list_filter = ['is_active', 'is_staff',('authentication__is_authenticated', admin.BooleanFieldListFilter),('authentication__is_pending', admin.BooleanFieldListFilter)]
    @admin.display(boolean=True,ordering=True)
    def is_authenticated(self, obj):
        return obj.authentication.is_authenticated
    
    is_authenticated.admin_order_field = "authentication__is_authenticated"

    @admin.display(boolean=True,ordering=True)
    def is_pending(self, obj):
        return obj.authentication.is_pending

    is_pending.admin_order_field = "authentication__is_pending"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(voteResults)