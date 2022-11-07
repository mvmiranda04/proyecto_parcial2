from django.urls import path
from .views import solicitud_vianda_create

app_name = 'vianda'
urlpatterns = [
    # vianda views
    # path('', vianda_lista, name='vianda_lista'),
    path('create/', solicitud_vianda_create, name='solicitud_vianda_create'),
]
