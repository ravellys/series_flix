from django import forms

from serieflix_project.genero.models import Genero


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
