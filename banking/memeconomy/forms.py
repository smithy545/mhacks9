from django import forms

class MemeForm(forms.Form):
	name = forms.CharField(label="Meme name", max_length=100)
	memepage = forms.CharField(label="Know your meme page", max_length=100)
	categories = forms.CharField(label="Comma-separated meme categories", max_length=200)