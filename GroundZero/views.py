from django.shortcuts import redirect, render

from .models import Artista, Genero

from .forms import GeneroForm

from django.shortcuts import render, get_object_or_404

from .forms import PinturaForm


# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

def our_jobs(request):
    return render(request, 'our_jobs.html')

def paintings(request):
    # Aquí podrías agregar lógica para mostrar pinturas específicas
    return render(request, 'paintings.html')

def sculptures(request):
    # Lógica para mostrar esculturas
    return render(request, 'sculptures.html')

def goldsmithing(request):
    # Lógica para mostrar orfebrería
    return render(request, 'goldsmithing.html')

def fabrics(request):
    # Lógica para mostrar tejidos
    return render(request, 'fabrics.html')

def know_us(request):
    return render(request, 'know_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def error_view(request):
    return render(request, 'error.html')

def artist_detail(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'artist_detail.html', {'artista': artista})

def search_results(request):
    # Aquí implementarías la lógica para obtener los resultados de búsqueda
    results = []  # Esta lista debe contener los resultados de la búsqueda
    context = {
        'results': results
    }
    return render(request, 'search_results.html', context)

def agregar_pintura(request):
    if request.method == 'POST':
        form = PinturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pinturas')  # Redirige a la página de listado de pinturas
    else:
        form = PinturaForm()
    
    return render(request, 'agregar_pintura.html', {'form': form})

def crear_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista')  # Reemplaza 'nombre_de_la_vista' con el nombre de la vista a la que quieres redirigir después de guardar el formulario
    else:
        form = GeneroForm()
    return render(request, 'nombre_de_la_plantilla.html', {'form': form})
