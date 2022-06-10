from dataclasses import field
from distutils.command.upload import upload
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
# from.models import Post


class SignUpForm(UserCreationForm):
	password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2= forms.CharField(label='Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	phonenumber=forms.CharField(label="Mobile")
	gumasta=forms.FileField(label='Gumasta')
	# name=forms.TextInput()
	class Meta(UserCreationForm.Meta):
		model = User
		fields=UserCreationForm.Meta.fields+('username',"phonenumber","first_name",'gumasta')
		label={'phonenumber':"Mobile","first_name":"Name",'gumasta':"Gumasta"}
		widgets ={'username': forms.TextInput(attrs={'class':'form-control'}),
		# 'name': forms.TextInput(attrs={'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'class':'form-control','required':True,}),
		# 'last_name': forms.TextInput(attrs={'class':'form-control','required':True,}),
		# 'email': forms.EmailInput(attrs={'class':'form-control','required':True,}),
		'phonenumber':forms.CharField(attrs={'class':'form-control','required'=True,}),
		'gumasta':forms.ImageField(),
		}

class LoginForm(AuthenticationForm):
	username=UsernameField(label='UserName',widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
	password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))