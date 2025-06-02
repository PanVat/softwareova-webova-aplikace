from django.apps import AppConfig

# Celá aplikace je tato třída
class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
