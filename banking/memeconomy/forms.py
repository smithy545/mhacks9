from django import forms

class MemeForm(forms.Form):
	memepage = forms.CharField(label="Know your meme page", max_length=100)
	categories = forms.CharField(label="Comma-separated meme categories", max_length=200)