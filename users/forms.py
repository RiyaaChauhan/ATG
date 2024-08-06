# myproject/users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, BlogPost
from users.models import User,BlogPost

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            self.add_error('password2', "Passwords do not match")

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
