from django import forms
from . models import AccountModel


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Enter Password' , widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    confirm_password = forms.CharField(label='Confirm Password' , widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    
    class Meta:
        model = AccountModel
        
        fields = ['first_name' , 'last_name' , 'username' , 'email' , 'phone_number', 'password' ]


        labels = {
            'first_name':'Enter First Name',
            'last_name':'Enter Last Name',
            'username' : 'Enter Username',
            'email' : 'Enter Email-ID',
            'phone_number' : 'Enter Contact Number',
            'password' : 'Enter Password',
        }

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Enter Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email-Id'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
        }

