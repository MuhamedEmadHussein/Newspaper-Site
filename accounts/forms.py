from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("age",)
        # Show UserName, Password, age but we want Email Too
        fields = [
            'username',
            'email',
            'age',
        ]
        # We don’t need to include the password fields 
        # because they are required!
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        
        fields = [
            'username',
            'email',
            'age',
        ]
        # We don’t need to include the password fields 
        # because they are required!
        