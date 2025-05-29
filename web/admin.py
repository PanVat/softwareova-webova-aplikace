from django.contrib import admin
from .models import Software, Vyvojar, Verze

# Registrace modelů do administrace Django
admin.site.register(Software)
admin.site.register(Vyvojar)
admin.site.register(Verze)
