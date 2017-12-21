from django import forms
class ContactForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)