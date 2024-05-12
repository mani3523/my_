from django import forms
from todolist.models import Todolist

class Taskform(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['task','done']