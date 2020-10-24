from django.urls import path

from serieflix_project.genero.views import cadastro

app_name = 'genero'
urlpatterns = [
    path('', cadastro, name='cadastro'),
]
