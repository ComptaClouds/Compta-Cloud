from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['denominations', 'sieges', 'objets', 'capitals', 'durees','name']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Compte)
admin.site.register(Piece)
admin.site.register(Credits)
admin.site.register(Debits)
admin.site.register(Users)
admin.site.register(Typejournal)
admin.site.register(Operation)
