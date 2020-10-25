from django.urls import path

from serieflix_project.series.views import cadastro, delete, update

app_name = 'series'
urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('delete/<id>', delete, name='delete'),
    path('update/<id>', update, name='update'),
]
