from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from serieflix_project.genero.forms import GeneroForm
from serieflix_project.genero.models import Genero


def cadastro(request):
    form = GeneroForm()
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            print('saving')
            form.save(commit=True)
            return redirect('/genero')
        else:
            print("error")

    genero_records = Genero.objects.order_by('descricao')
    return render(request, 'genero/genero.html',
                  context={"form": form, "genero_records": genero_records})


def delete(request, id):
    try:
        Genero.objects.filter(id=id).delete()
        form = GeneroForm()
        genero_records = Genero.objects.order_by('descricao')
        data_dict = {"genero_records": genero_records, 'form': form}
        return render(request, 'genero/genero.html', data_dict)
    except not id:
        return HttpResponseNotAllowed()


def update(request, id):
    item = Genero.objects.get(id=id)
    if request.method == "GET":
        form = GeneroForm(initial={'descricao': item.descricao})
        data_dict = {'form': form}
        return render(request, 'genero/genero_update.html', data_dict)
    else:
        form = GeneroForm(request.POST)
        item.descricao = form.data['descricao']
        item.save()
        generos_list = Genero.objects.order_by('descricao')
        data_dict = {"genero_records": generos_list, 'form': form}
        return render(request, 'genero/genero.html', data_dict)
