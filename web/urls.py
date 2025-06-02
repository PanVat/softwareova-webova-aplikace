from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), ## Výchozí routa pro hlavní stránku
    path('record/<int:pk>/', views.record, name='record'), ## Routa pro detail záznamu
    path('software/add/', views.software_add, name='software_add'), ## Routa pro přidání nového záznamu
    path('software/<int:pk>/edit/', views.software_edit, name='software_edit'), ## Routa pro úpravu záznamu
    path('software/<int:pk>/delete/', views.software_delete, name='software_delete'), ## Routa pro smazání záznamu
]
