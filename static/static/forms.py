from django import forms

class create_form(forms.Form):
	inupt_dict = forms.CharField(label='Your name', max_length=100)
	inupt_dict1 = forms.CharField(label='You', max_length=100)
	message = forms.CharField()
	