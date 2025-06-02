from django.db import models

## Třída pro typy verzí softwaru ##
class Typ(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Typ verze', help_text='Zadejte typ verze',
                             error_messages={'blank': 'Typ verze nemůže být prázdný'})

    # Třída pro metadata
    class Meta:
        verbose_name = 'Typ verze'
        verbose_name_plural = 'Typy verzí'
        ordering = ['nazev']

    # Textová reprezentace objektu
    def __str__(self):
        return self.nazev