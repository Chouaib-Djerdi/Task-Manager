from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'created')
        labels = {
            'title':'Title:',
            'description':'Description:',
            'created':'Created:',
        }
        exclude = ['manager']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'created': forms.DateInput(attrs={'class':'form-control', 'placeholder':'MM/DD/YY'})
        }
        #we are converting this to modelform concept
        #complete the wigdets
        #change the type of date used
        #update the views 

