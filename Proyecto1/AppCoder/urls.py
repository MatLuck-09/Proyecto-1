from django.urls import path, include
from AppCoder.views import inicio,cursos,entregables,estudiantes,profesores

urlpatterns = [
    path('inicio/', inicio),
    path('curso/', cursos),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('profesores/', profesores),
]