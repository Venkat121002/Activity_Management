from django import forms

class RegistrationForm(forms.Form):

    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    firstname = forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(max_length=50,required=False,widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,required=True,widget=forms.Select(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

