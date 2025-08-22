from django import forms

class ProfileForm(forms.Form):
    headline = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    skills = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))

