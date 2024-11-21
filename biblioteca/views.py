from django.shortcuts import render
from .models import Libro

def mostrar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'mostrar_libros.html', {'libros': libros})