from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#extends UserAdmin to use our new CustomUser model instaed of User model.
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
   
    model = CustomUser
    # to use CustomUser Model instead of User model
   
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    # To control which fields are listed

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)
    # to actually edit and add new custom fields like age
    # fieldsets (for fields used in editing users). 
    # add_fieldsets(for fields used when creating a user).
admin.site.register(CustomUser,CustomUserAdmin)    



