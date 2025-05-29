from django.db import models
from multiselectfield import MultiSelectField
from . import moznosti  # Importuje možnosti volby


# Třída pro ukládání dat jednotlivých programů
class Software(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název', help_text='Zadejte název programu',
                             error_messages={'blank': 'Název nemůže být prázdný'})
    kategorie = MultiSelectField(choices=moznosti.KATEGORIE, verbose_name='Kategorie', blank=True, null=True)
    vydani = models.DateField(verbose_name='Datum vydání', blank=True, null=True)
    licence = MultiSelectField(choices=moznosti.LICENCE, verbose_name='Licence', blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena (Kč)', blank=True, null=True, )
    jazyk = MultiSelectField(choices=moznosti.JAZYK, verbose_name='Jazyk', blank=True, null=True)
    platforma = MultiSelectField(choices=moznosti.PLATFORMA, verbose_name='Platforma', blank=True, null=True)
    popis = models.TextField(verbose_name='Popis', help_text='Stručně popište program', blank=True, null=True)
    ikona = models.ImageField(upload_to='ikony', verbose_name='Ikona', blank=True, null=True)
    # Cizí klíč na vývojáře
    vyvojar = models.ForeignKey('Vyvojar', on_delete=models.CASCADE, verbose_name='Vývojář', blank=True, null=True)

    # Třída pro metadata
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programy'
        ordering = ['nazev']

    # Textová reprezentace objektu
    def __str__(self):
        return self.nazev


# Třída pro ukládání dat jednotlivých vývojářů programů
class Vyvojar(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno', help_text='Zadejte jméno nebo přezdívku vývojáře',
                             error_messages={'blank': 'Pole nemůže být prázdné'})
    email = models.EmailField(verbose_name='E-mail', help_text='Zadejte e-mailovou adresu vývojáře')
    web = models.URLField(verbose_name='Web', help_text='Zadejte URL adresu webové stránky vývojáře', blank=True,
                          null=True)
    informace = models.TextField(verbose_name='Informace', help_text='Zadejte informace o vývojáři', blank=True,
                                 null=True)
    profil = models.ImageField(upload_to='profily', verbose_name='Profilový obrázek', blank=True, null=True)

    # Třída pro metadata
    class Meta:
        verbose_name = 'Vývojář'
        verbose_name_plural = 'Vývojáři'
        ordering = ['jmeno']

    # Textová reprezentace objektu
    def __str__(self):
        return self.jmeno


# Třída pro ukládání dat jednotlivých verzí programů
class Verze(models.Model):
    # Cizí klíč na program
    software = models.ForeignKey('Software', on_delete=models.CASCADE, verbose_name='Software', blank=True, null=True)
    verze = models.CharField(max_length=30, verbose_name='Verze', help_text='Zadejte verzi programu',
                             error_messages={'blank': 'Pole nemůže být prázdné'})
    vydani = models.DateField(verbose_name='Datum vydání', blank=True, null=True)
    typ = MultiSelectField(choices=moznosti.TYP, verbose_name='Typ verze', blank=True, null=True)
    popis = models.TextField(verbose_name='Popis', help_text='Zadejte popis verze', blank=True, null=True)
    velikost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Velikost (MB)', blank=True, null=True)

    # Třída pro metadata
    class Meta:
        verbose_name = 'Verze'
        verbose_name_plural = 'Verze'
        ordering = ['software', 'verze']

    # Textová reprezentace objektu
    def __str__(self):
        return f"{self.software.nazev} – {self.verze}"
