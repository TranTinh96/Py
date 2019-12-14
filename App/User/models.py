from django import forms

# Create your models here.

class ContactForm(forms.Form):
   full_name = forms.CharField()
   email =forms.EmailField()
   content = forms.CharField(widget=forms.Textarea)
