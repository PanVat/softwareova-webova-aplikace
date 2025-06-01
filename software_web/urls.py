from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('software/', include('web.urls')),
    path('', RedirectView.as_view(url='/software/'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)