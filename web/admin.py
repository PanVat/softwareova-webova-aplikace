from django.contrib import admin
from .models import Software, Verze, SystemovePozadavky
from .seznamy_software import Kategorie, Licence, Jazyk, Platforma
from .seznamy_verze import Typ

# Registrace modelů do administrace Django
admin.site.register(Software)
admin.site.register(Verze)
admin.site.register(Kategorie)
admin.site.register(Licence)
admin.site.register(Jazyk)
admin.site.register(Platforma)
admin.site.register(Typ)
admin.site.register(SystemovePozadavky)
