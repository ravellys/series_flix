from django.shortcuts import render
from serieflix_project.genero.forms import GeneroForm


def cadastro(request):
    form = GeneroForm()
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("eRROR")

    return render(request, 'genero/genero.html', context={"form": form})
