from django.shortcuts import render, get_object_or_404, redirect

from .forms import SoftwareForm
from .models import Software, Verze
from . import seznamy_software as sez_soft


## Hlavní stránka, kde se zobrazuje posledních 8 přidaných záznamů ##
def index(request):
    kategorie_nazev = request.GET.get('kategorie')
    kategorie_obj = None

    if kategorie_nazev and kategorie_nazev != "Vše":
        kategorie_obj = sez_soft.Kategorie.objects.filter(nazev=kategorie_nazev).first()
        if kategorie_obj:
            software_qs = Software.objects.filter(kategorie=kategorie_obj).order_by('-id')[:8]
        else:
            software_qs = []
    else:
        software_qs = Software.objects.all().order_by('-id')[:8]

    # Pole se naplní přesně na 8 položek
    software_list = list(software_qs)
    while len(software_list) < 8:
        software_list.append(None)

    vsechny_kategorie = sez_soft.Kategorie.objects.all()

    context = {
        'software_list': software_list,
        'kategorie_aktivni': kategorie_nazev or "Vše",
        'kategorie_vsechny': vsechny_kategorie,
        'verze': Verze.objects.all(),
    }
    return render(request, 'index.html', context)


## Detail záznamu, kde se zobrazí všechny informace o programu ##
def record(request, pk):
    program = get_object_or_404(Software, pk=pk)
    return render(request, 'record.html', {'program': program})


## Routa pro přidání nového záznamu do databáze ##
def software_add(request):
    if request.method == "POST":
        form = SoftwareForm(request.POST, request.FILES)
        if form.is_valid():
            program = form.save()
            return redirect('record', pk=program.pk)
    else:
        form = SoftwareForm()
    return render(request, 'software_add.html', {'form': form})


## Routa pro smazání záznamu z databáze ##
def software_delete(request, pk):
    program = get_object_or_404(Software, pk=pk)
    if request.method == "POST":
        program.delete()
        return redirect('index')
    # Bez potvrzovací stránky, smaže přímo po POST
    return redirect('record', pk=program.pk)


## Routa pro úpravu záznamu v databázi ##
def software_edit(request, pk):
    program = get_object_or_404(Software, pk=pk)
    if request.method == "POST":
        form = SoftwareForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect('record', pk=program.pk)
    else:
        form = SoftwareForm(instance=program)
    return render(request, 'software_edit.html', {'form': form, 'program': program})
