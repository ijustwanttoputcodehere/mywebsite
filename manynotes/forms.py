from django import forms
from django.forms import Select

from .models import Notes


class NoteForm(forms.ModelForm):

    class Meta:

        model = Notes
        fields = ('title', 'author', 'pdf', 'category')



       # widgets = {
        #    'routineType': forms.Select(choices=CATEGORIES),
        #    'pointA': forms.TextInput(attrs={'placeholder': 'xx,xx', 'value': '0'}),
        #    'pointB': forms.TextInput(attrs={'placeholder': 'xx,xx', 'value': '0'}),
        #    'pointC': forms.TextInput(attrs={'placeholder': 'xx,xx', 'value': '0'}),
       # }


