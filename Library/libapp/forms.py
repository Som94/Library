from django import forms
from libapp.models import LibraryModel

class LibraryForm(forms.ModelForm):
    class Meta:
        model=LibraryModel
        fields='__all__'
