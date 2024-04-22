from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    apply_as_seller = forms.BooleanField(required=False, help_text='Check if you want to apply as a seller.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'apply_as_seller')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.seller_status = 'pending' if self.cleaned_data['apply_as_seller'] else 'default'
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=255)


