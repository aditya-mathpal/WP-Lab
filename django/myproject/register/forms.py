from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        label="User Name",
        max_length=100,
        required=True
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=False
    )
    
    email = forms.EmailField(
        label="Email",
        required=False
    )
    
    contact = forms.CharField(
        label="Contact Number",
        max_length=10,
        required=False
    )