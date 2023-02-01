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
        #we are converting this to modelform concept
        #complete the wigdets
        #change the type of date used
        #update the views 

