from django import forms

class UserRegistrationForm(forms.Form):
    user=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()


class UserLoginForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()