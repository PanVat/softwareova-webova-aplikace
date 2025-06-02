from django.shortcuts import render, get_object_or_404

from .models import Software, Verze
from . import seznamy_software as sez_soft


# Hlavní stránka, kde se zobrazují všechny přidané záznamy
def index(request):
    kategorie_nazev = request.GET.get('kategorie')
    kategorie_obj = None

    if kategorie_nazev and kategorie_nazev != "Vše":
        kategorie_obj = sez_soft.Kategorie.objects.filter(nazev=kategorie_nazev).first()
        if kategorie_obj:
            software = Software.objects.filter(kategorie=kategorie_obj)
        else:
            software = Software.objects.none()
    else:
        software = Software.objects.all()

    # Získání všech kategorií pro menu:
    vsechny_kategorie = sez_soft.Kategorie.objects.all()

    context = {
        'software': software,
        'kategorie_aktivni': kategorie_nazev or "Vše",
        'kategorie_vsechny': vsechny_kategorie,
        'verze': Verze.objects.all(),
    }
    return render(request, 'index.html', context)


# Detail záznamu, kde se zobrazí všechny informace o programu

def record(request, pk):
    program = get_object_or_404(Software, pk=pk)
    return render(request, 'record.html', {'program': program})
