from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UsernameField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_active', 'is_blocked', 'is_superuser', ]

    def clean_password(self):
        return self.initial["password"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control', 'id': 'email'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','id': 'password1'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','id': 'password2'}))

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False # Email verification
        if commit:
            user.save()
        return user
