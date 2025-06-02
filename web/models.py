from django.db import models
from . import seznamy_software as sez_soft  # Import modulu, který obsahuje více možností pro tabulku 'Software'
from . import seznamy_verze as sez_ver  # Import modulu, který obsahuje více možností pro tabulku 'Verze'


## Třída pro ukládání záznamů o programech ##
class Software(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název', help_text='Zadejte název programu',
                             error_messages={'blank': 'Název nemůže být prázdný'})
    kategorie = models.ManyToManyField(sez_soft.Kategorie, verbose_name='Kategorie',
                                       help_text='Zadejte název kategorie')
    vydani = models.DateField(verbose_name='Datum vydání', blank=True, null=True)
    licence = models.ManyToManyField(sez_soft.Licence, verbose_name='Licence', help_text='Zadejte název licence')
    cena = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena (Kč)', blank=True, null=True, )
    jazyk = models.ManyToManyField(sez_soft.Jazyk, verbose_name='Jazyk', help_text='Zadejte jazyk programu')
    platforma = models.ManyToManyField(sez_soft.Platforma, verbose_name='Platforma',
                                       help_text='Zadejte název platformy')
    popis = models.TextField(verbose_name='Popis', help_text='Stručně popište program', blank=True, null=True)
    ikona = models.ImageField(upload_to='ikony', verbose_name='Ikona', blank=True, null=True)
    url = models.URLField(verbose_name='URL', help_text='Zadejte URL adresu programu', blank=True, null=True)

    # Třída pro metadata
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programy'
        ordering = ['nazev']

    # Textová reprezentace objektu
    def __str__(self):
        return self.nazev


## Třída pro ukládání systémových požadavků programu ##
class SystemovePozadavky(models.Model):
    program = models.ForeignKey('Software', on_delete=models.CASCADE, verbose_name='Program', blank=True, null=True)
    cpu = models.CharField(max_length=100, verbose_name='Procesor', help_text='Procesor', blank=True, null=True)
    gpu = models.CharField(max_length=100, verbose_name='Grafická karta', help_text='Grafická karta',
                           blank=True, null=True)
    vram = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Video paměť (GB)', blank=True, null=True)
    ram = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='RAM (GB)', blank=True, null=True)
    disk = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Disk (GB)', blank=True, null=True)
    os = models.CharField(max_length=100, verbose_name='Operační systém', help_text='Operační systém',
                          blank=True, null=True)

    # Třída pro metadata
    class Meta:
        verbose_name = 'Systémové požadavky'
        verbose_name_plural = 'Systémové požadavky'
        ordering = ['cpu']

    # Textová reprezentace objektu
    def __str__(self):
        return f"{self.cpu}, {self.gpu}, {self.ram}, {self.disk}, {self.os}"


## Třída pro uložení verze programu ##
class Verze(models.Model):
    # Cizí klíč na program
    software = models.ForeignKey('Software', on_delete=models.CASCADE, verbose_name='Software', blank=True, null=True)
    verze = models.CharField(max_length=30, verbose_name='Verze', help_text='Zadejte verzi programu',
                             error_messages={'blank': 'Pole nemůže být prázdné'})
    vydani = models.DateField(verbose_name='Datum vydání', blank=True, null=True)
    typ = models.ManyToManyField(sez_ver.Typ, verbose_name='Typ verze', help_text='Zadejte typ verze')
    popis = models.TextField(verbose_name='Popis', help_text='Zadejte popis verze', blank=True, null=True)
    velikost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Velikost (MB)', blank=True, null=True)

    # Třída pro metadata
    class Meta:
        verbose_name = 'Verze'
        verbose_name_plural = 'Verze'
        ordering = ['software', 'verze']

    # Textová reprezentace objektu
    def __str__(self):
        return f"{self.software.nazev if self.software else ''} – {self.verze}"
