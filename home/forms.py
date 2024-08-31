from django import forms

from .models import TODO

class CreateTodoForms(forms.Form):
    title=forms.CharField()
    body=forms.CharField()
    created=forms.DateField()
    

class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model=TODO
        fields=['title','body','created']







