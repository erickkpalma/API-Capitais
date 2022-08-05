from django.urls import path

from .views import EstadosAPI

urlpatterns = [
    path('estados/', EstadosAPI.as_view(), name='estados')
]