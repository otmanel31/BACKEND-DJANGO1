from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Repas)
admin.site.register(ElementRepas)

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Nutriuser

class UserCreateForm(UserCreationForm):
    class Meta:
        model = Nutriuser
        fields = ('height', 'weight')

class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    #prepopulated_fields = {username('first_name', 'last_name')}
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('height', 'weight', 'username', 'password1', 'password2', ),
            }),
        )
#admin.site.register(Nutriuser, UserAdmin)
class NutriuserAdmin(UserAdmin): #admin.ModelAdmin):
    #model = Nutriuser
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('height', 'weight', 'bmi', 'rda', 'birthdate')}),
    )
admin.site.register(Nutriuser, NutriuserAdmin)
#admin.site.register(Nutriuser, UserAdmin)