from django.urls import path

from serieflix_project.genero.views import cadastro, delete, update

app_name = 'genero'
urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('delete/<id>', delete, name='delete'),
    path('update/<id>', update, name='update'),
]
