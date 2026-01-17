from django.contrib import admin
from . import models as m 
from django.contrib.auth.models import User

admin.site.register(m.Category)
admin.site.register(m.Customer)
admin.site.register(m.Product)
admin.site.register(m.Order)
admin.site.register(m.Profile)



class ProfileInline(admin.StackedInline):
    model = m.Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]


# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)

