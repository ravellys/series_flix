from django import forms

from serieflix_project.series.models import Serie


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'
