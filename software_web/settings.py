from pathlib import Path
import os

# Základní adresář projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# Tajný klíč, který vystavuji veřejně jen pro demonstrační účely
SECRET_KEY = 'django-insecure-*i)*)6b8!8oto@6iv@(p1!%hsnt@9h$=fgnbqq4^+@xnci!z*_'

# Pokud se aplikace spouští v produkčním prostředí, má být 'False', jinak 'True'
# Když je 'False', nebude obsluhovat statické soubory
DEBUG = True

ALLOWED_HOSTS = []

# Instalované aplikace
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web.apps.WebConfig'  # Důležité pro moji aplikaci
]

# Nějaké další balíčky, které by mohly být užitečné
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Kořenová URL konfigurace
ROOT_URLCONF = 'software_web.urls'

# Nastavení pro šablony
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI aplikace
WSGI_APPLICATION = 'software_web.wsgi.application'

# Nastavení databáze a koncovky souboru
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validátory pro hesla
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Jazyk a časové pásmo
LANGUAGE_CODE = 'cs-cz'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_TZ = True

# Statické soubory (obrázky, CSS, JS atd.)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Nahrané soubory (ikonky programů atd.)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
