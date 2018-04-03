from django import forms
from .models import User
import bcrypt

class regForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2
    )
    last_name = forms.CharField(
        min_length=2
    )
    email = forms.EmailField(
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput()
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password_confirm')
    
    def clean(self):
        cleaned = self.cleaned_data
        if cleaned['password'] != cleaned['password_confirm']:
            raise forms.ValidationError(
                "password and confirm password must match"
            )
        else:
            cleaned['password'] = bcrypt.hashpw(cleaned['password'].encode(), bcrypt.gensalt())
        if len(User.objects.filter(email=cleaned['email'])) > 0:
            raise forms.ValidationError(
                "Email is already in use"
            )

class loginForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    class Meta:
        model = User
        fields = ('email', 'password')
    
    def clean(self):
        cleaned = self.cleaned_data
        this_user = User.objects.get(email=cleaned['email'])

        if not this_user:
            raise forms.ValidationError(
                "Email does not exist"
            )
        this = this_user.password
        check = cleaned['password']
        if bcrypt.checkpw(check.encode(), this.encode()) == False:
            raise forms.ValidationError(
                "wrong password"
            )

   
    

