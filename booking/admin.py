from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Movie, Theater, Screening, Booking

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "user_id",
        "email",
        "date_birth",
        "phone_number",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("date_birth", "phone_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ( "date_birth", "phone_number",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Screening)
admin.site.register(Booking)

