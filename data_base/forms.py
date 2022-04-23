from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class HashForm(forms.Form):
    hash_number = forms.CharField(label="Hash Diploma", max_length=256)

class UploadFileForm(forms.Form):
    file = forms.FileField()