from django import forms
from django.contrib.auth.models import User
# from django.core import validators

class SignUpForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


    # class Meta:
    #     model=User
    #     fields=['FirstName','LastName','Password','Repassword','Email','ContactNo']
    #
    #     FirstName=forms.CharField(max_length=100)
    #     LastName=forms.CharField(max_length=100)
    #     Password=forms.CharField(max_length=100)
    #     Repassword=forms.CharField(max_length=100)
    #     Email=forms.EmailField()
    #     ContactNo=forms.IntegerField()
    #
    #
    #     def clean(self):
    #         total_clean_data=super().clean()
    #         pwd=total_clean_data['Password']
    #         if len(pwd)<8:
    #             raise forms.ValidationError("Password Length Must be Greater than or Equal to 8")
    #         rpwd=total_clean_data['Repassword']
    #         if pwd!=rpwd:
    #             raise forms.ValidationError("Both Password Should Be Match..")
