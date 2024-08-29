from django import forms

class CreateTodoForms(forms.Form):
    title=forms.CharField()
    body=forms.CharField()
    created=forms.DateField()
    
    







