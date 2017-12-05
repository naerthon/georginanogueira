from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
	class Meta:
	    model = Email
	    fields = ['full_name','ddd','phone','message','email',]
	    widgets = {
	        'full_name' : forms.TextInput(attrs={
	            'placeholder':'Nome Compelto',
	            'class':'form-control',
	            'required' : 'required',
	        }),
	        'email' : forms.TextInput(attrs={
	            'placeholder':'Email',
	            'class':'form-control',
	            'required' : 'required',
	        }),
	        'ddd' : forms.TextInput(attrs={
	            'placeholder':'DDD',
	            'class':'form-control',
	            'required' : 'required',
	        }),
	        'phone' : forms.TextInput(attrs={
	            'placeholder':'Telefone',
	            'class':'form-control',
	            'required' : 'required',
	        }),
	        'message' : forms.Textarea(attrs={
	            'placeholder':'Mensagem',
	            'class':'form-control',
	            'required' : 'required',
	        }),
	    }