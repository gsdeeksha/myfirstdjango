from django import forms
from home.models import Book,Author,Genre

class CustomForms(forms.Form):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(attrs = {'placeholder':'Your username','class':'form.control','max':'20'
            }
        )
    )
    email = forms.EmailField(label="your Email",widget=forms.EmailInput(attrs={'placeholder':'ac@mail.com','class':'form-control'}))

class BookForms(forms.Form):
    name= forms.CharField(label='Book name',widget= forms.TextInput(attrs={'maxlength' :'30', 'placeholder':'Book Name','class':'form-control','autofocus':'true'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Author', widget= forms.Select(attrs={'name':'author','id':'author','class':'custom-select'}))
    pur_date=forms.DateField(label='',widget= forms.DateInput(attrs={'placeholder':'purchase date','name':'pur_date','id':'pur_date','class':'form-control'}))
    # summary = forms.CharField(label='Summary',
    #                    widget = forms.Textarea(attrs={'placeholder':'Summary','name':'summary',
    #                    'id':'summary','class':'form-control'}))
    # isbn = forms.CharField(label='ISBN number',
    #                    widget=forms.TextInput(attrs={'placeholder':'ISBN Number',
    #                    'class':'form-control','name':'isbn','id':'isbn'}))
    # genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
    #                    widget=forms.CheckboxSelectMultiple)



class ModelBookForms(forms.ModelForm):
    name= forms.CharField(label='Book name',widget= forms.TextInput(attrs={'maxlength' :'30', 'placeholder':'Book Name','class':'form-control'}))
    author = forms.ModelChoiceField(queryset= Author.objects.all(),empty_label='Author', widget= forms.Select(attrs={'name':'author','id':'author','class':'custom-select'}))
    pur_date=forms.DateField(label='',widget= forms.DateInput(attrs={'placeholder':'purchase date','name':'pur_date','id':'pur_date','class':'form-control'}))
    
    class Meta:
        model = Book
        fields = ('name','purchase_date','genre','author')
        # fields = '__all__'

class SearchForm(forms.Form):
    q = forms.CharField(label='Book Name',widget= forms.TextInput(attrs={'maxlength' :'30', 'placeholder':'Search','class':'form-control','minlength':'2'}))



# from django import forms
# from home.models import newreg,login    

# class loginForms(forms.Form):
#     username = forms.CharField(
#         label = 'Username',
#         widget = forms.TextInput(attrs = {'placeholder':'Your username','class':'form.control','max':'20'
#             }
#         )
#     )
#     password = forms.charField(label="your password",widget=forms.TextInput(attrs=
#      {'placeholder':'password','class':'form-control'}))
    
# class registerForms(forms.Form):
#     username = forms.CharField(
#         label = 'Username',
#         widget = forms.TextInput(attrs = {'placeholder':'Your username','class':'form.control','max':'20'
#             }
#         )
#     )
#     password = forms.charField(label="your password",widget=forms.TextInput(attrs=
#      {'placeholder':'password','class':'form-control'}))
#     confirm_password = forms.charField(label="your confirm-password",widget=forms.TextInput(attrs=
#      {'placeholder':'Confirm password','class':'form-control'}))
#     email = forms.EmailField(label="your Email",widget=forms.EmailInput(attrs=
#      {'placeholder':'ac@mail.com','class':'form-control'}))




# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
 
# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
 
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
 
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
 
#         if commit:
#             user.save()
 
#         return user