from django import forms
from django.contrib.auth.models import User

class emailForm(forms.Form):
    #class meta:
     #   model = User
      #  fields= ['email']   required=True,
    #email = forms.CharField( label='Email address:')#, placeholder = "example@gmail.com")

    email = forms.CharField(max_length=100, label="Change your email:",
                                 widget=forms.TextInput
                                 (attrs={'class': 'form-control',
                                         'required': True,
                                         'placeholder': "example@gmail.com",
                                         'type': 'email',
                                         }))
