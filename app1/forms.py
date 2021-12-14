from django import forms
from django.forms import fields, widgets
from app1.models import  Pin,User
from django.contrib.auth.forms import UserChangeForm,SetPasswordForm,UserCreationForm,AuthenticationForm
# from django.contrib.auth.models import User


class updateForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ['username','first_name','last_name','email','year','dept','semester','enrollment','profilepic']

        widgets={
            'pin':forms.FileInput(attrs={
                'class':"form-control-file"
            })
        }

          
       


         
class createPinForm(forms.ModelForm):
    class Meta:
        model=Pin
        fields='__all__'

        

        widgets={

            'heading':forms.TextInput(attrs={
                'class':"form-control",
                'id':"pin-title",
                'placeholder':"Add title"
            }),
            'tag':forms.TextInput(attrs={
                'class':"form-control",
                'id':"pin-title",
                'placeholder':"Add tag"
            }),

            'details':forms.Textarea(attrs={
                'class':"form-control",
                'style':"max-height: 200px; min-height: 200px; weight:100px;",
                'id':"exampleTextarea",
                 'rows':"6"
            }),
            'pin':forms.FileInput(attrs={
                'class':"form-control-file",
                'style':"visibility:hidden;",
                'id':"pin-picture"
            })


        }



 



class signupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input',
            'placeholder': "First Name......."
        }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input',
            'placeholder': "Last Name............."
        }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input',
            'placeholder': "User Name ..."
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control input',
            'placeholder': "Email....."
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control input',
            'placeholder': "Password...."
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control input',
            'placeholder': "Confirm Password..."
        }
    ))

    

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2',
                  'is_cdc', 'is_teacher', 'is_student','profilepic')





class signinForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

        widgets={
            'username':forms.TextInput(attrs={
                'id':"user",
                'class':"form-control input",
                'placeholder':'Enter username',
                }),

            'password':forms.PasswordInput(attrs={
                'id':"pass",
                'class':"form-control input",
                'placeholder':'Enter Password',
                'data-type':"password"
                })
        
        }


class changePasswordForm(SetPasswordForm):
    new_password2=forms.CharField(label='Confirm New password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields='__all__'
    