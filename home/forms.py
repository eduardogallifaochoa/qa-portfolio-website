from django import forms

TOPICS = [
    ("QA_MANUAL", "QA Manual"),
    ("QA_AUTO", "QA Automation"),
    ("QA_BOTH", "QA Manual + Automation"),
    ("QA_LEAD", "QA Lead"),
]

class ContactForm(forms.Form):
    topic = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), choices=TOPICS)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=200)
    message = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control'}), max_length=2000)
