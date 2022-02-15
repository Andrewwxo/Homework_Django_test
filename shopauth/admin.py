from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from shopauth.models import ShopUser


# admin.site.register(ShopUser)
class ShopUserAdmin(UserAdmin):
    pass


admin.site.register(ShopUser, ShopUserAdmin)
