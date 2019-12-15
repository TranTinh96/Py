from django import forms

class ContactHome(forms.Form):
   full_name = forms.CharField()
   email = forms.EmailField()
   content = forms.CharField(widget=forms.Textarea)

   # Validate Data on Fields
   def clean_email(self,*args, **kwargs):
      email = self.cleaned_data.get('email')
      print(email)
      if email.endswith(".edu"):
         raise forms.ValidationError("This is not a valid email . Please don't not .edu")
      return email