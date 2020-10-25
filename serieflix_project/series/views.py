from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect

# Create your views here.
from serieflix_project.series.forms import SerieForm
from serieflix_project.series.models import Serie


def cadastro(request):
    form = SerieForm()
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            print('saving')
            form.save(commit=True)
            return redirect('/series')
        else:
            print("error")

    series_records = Serie.objects.order_by('nome')
    return render(request, 'series/series.html',
                  context={"form": form, "series_records": series_records})


def delete(request, id):
    try:
        Serie.objects.filter(id=id).delete()
        form = Serie()
        series_records = Serie.objects.order_by('nome')
        data_dict = {"series_records": series_records, 'form': form}
        return render(request, 'series/series.html', data_dict)
    except not id:
        return HttpResponseNotAllowed()


def update(request, id):
    item = Serie.objects.get(id=id)
    if request.method == "GET":
        form = SerieForm(initial={'nome': item.nome})
        data_dict = {'form': form}
        return render(request, 'series/series_update.html', data_dict)
    else:
        form = SerieForm(request.POST)
        print(item)
        item.nome = form.data['nome']
        print(item)
        item.idGenero.id = form.data['idGenero']
        item.save()
        serie_list = Serie.objects.order_by('nome')
        data_dict = {"series_records": serie_list, 'form': form}
        return render(request, 'series/series.html', data_dict)
