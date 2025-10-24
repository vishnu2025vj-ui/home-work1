from django import forms

class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        label="Full Name",
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': ' full Enter  name'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'})
    )
    password = forms.CharField(
        label="Password",
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )
