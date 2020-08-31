from django import forms
from .models import User_Profile

#File_Upload
class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'first_name',
        'last_name',
        'nickname',
        'technologies',
        'email',
        'display_picture'
        ]