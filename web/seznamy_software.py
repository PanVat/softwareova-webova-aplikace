from django.db import models


# Ukládání jednotlivých názvů kategorií
class Kategorie(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název kategorie', help_text='Zadejte název kategorie',
                             error_messages={'blank': 'Název kategorie nemůže být prázdný'})

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


# Ukládání jednotlivých názvů licencí
class Licence(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název licence', help_text='Zadejte název licence',
                             error_messages={'blank': 'Název licence nemůže být prázdný'})

    class Meta:
        verbose_name = 'Licence'
        verbose_name_plural = 'Licence'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


# Ukládání jednotlivých názvů jazyků
class Jazyk(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název jazyka', help_text='Zadejte název jazyka',
                             error_messages={'blank': 'Název jazyka nemůže být prázdný'})
    zkratka = models.CharField(max_length=3, verbose_name='Zkratka jazyka', help_text='Zadejte zkratku jazyka')
    vlajka = models.ImageField(upload_to='vlajky', verbose_name='Vlajka jazyka')

    class Meta:
        verbose_name = 'Jazyk'
        verbose_name_plural = 'Jazyky'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


# Ukládání jednotlivých názvů platforem
class Platforma(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název platformy', help_text='Zadejte název platformy',
                             error_messages={'blank': 'Název platformy nemůže být prázdný'})

    class Meta:
        verbose_name = 'Platforma'
        verbose_name_plural = 'Platformy'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev
