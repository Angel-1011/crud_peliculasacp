from django.shortcuts import render, redirect, get_object_or_404
from .models import peliculas
from .forms import PeliculaForm, RegistroForm
import os
#Para los reportes
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
import datetime
#Para el login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q

# Create your views here.

@login_required
def create_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect(pelicula_list)  
    else:
        form = PeliculaForm()  

    return render(request, 'peliculas/pelicula_form.html', {'form': form})

def pelicula_list(request):
    query = request.GET.get("q")
    if query:
        peliculas_lista = peliculas.objects.filter(
            Q(nombre__icontains=query) | Q(categoria__icontains = query)
        )
    else:
        peliculas_lista = peliculas.objects.all()  
    return render(request, 'peliculas/pelicula_list.html', {'peliculas': peliculas_lista})
@login_required
def update_pelicula(request, pk):
    pelicula = get_object_or_404(peliculas, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect(pelicula_list)
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/pelicula_form.html',{'form': form, 'pelicula': pelicula})
@login_required
def delete_pelicula(request, pk):
    pelicula = get_object_or_404(peliculas, pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        return redirect(pelicula_list)
    return render(request, 'peliculas/pelicula_confirm_delete.html', {'pelicula': pelicula})
    #Reportes
def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    # abrir = inline, descargar = attachment
    response['Content-Disposition'] = 'inline; filename="peliculas.pdf"'

    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    pdf.setTitle("Reporte de peliculas")
    fecha_generacion = datetime.date.today().strftime("%d-%m-%Y")
    pagina_num = 1

    def pie_pagina(pdf, pagina_num):
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, 20, f"Fecha de generacion: {fecha_generacion}")
        pdf.drawString(width -100, 20, f"Pagina num. {pagina_num}")

    # Titulo del reporte centrado
    pdf.setFont("Helvetica-Bold", 16)
    texto = "Lista de peliculas"
    ancho_texto = pdf.stringWidth(texto)
    x = (width - ancho_texto) / 2
    pdf.drawString(x, height -40, texto)

    # Ruta a la imagen en la carpeta pdf/imagenes
    image_path = os.path.join("peliculas", "pdf", "imagenes", "imagen2.webp")

    # Insertar la imagen
    if os.path.exists(image_path):
        pdf.drawImage(image_path, 95, height - 60, width=50, height=50) # Ajustar la posición y el tamaño
    
    #Encabezados de la tabla
    encabezados = ["Nombre", "Categoria", "Año"]
    x_inicial = 100
    y = height -80
    pdf.setFont("Helvetica-Bold", 12)
    for i, encabezado in enumerate(encabezados):
        pdf.drawString(x_inicial + i * 150, y, encabezado)

    y -=10
    pdf.line(100, y, width-100,y)
    #Contenido
    y -=20
    query = request.GET.get("q")
    if query:
        peliculas_lista = peliculas.objects.filter(
            Q(nombre__icontains=query) | Q(categoria__icontains = query)
        )
    else:
        peliculas_lista = peliculas.objects.all()  
    
    pdf.setFont("Helvetica", 12)
    for pelicula in peliculas_lista:
        pdf.drawString(100, y, pelicula.nombre)
        pdf.drawString(250, y, pelicula.categoria)
        pdf.drawString(400, y, pelicula.año.strftime("%d-%m-%Y"))
        y -=20

        if y <= 50:
            pie_pagina(pdf, pagina_num)
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = height -80

            # Dibujar la imagen en la nueva página
            if os.path.exists(image_path):
                pdf.drawImage(image_path, 0, height - 100, width=100, height=100) 
                
            for i, encabezado in enumerate(encabezados):
                pdf.drawString(x_inicial + i * 150, y, encabezado)

            y -=10
            pdf.line(100, y, width-100,y)
            y -=20

            pagina_num += 1

    pie_pagina(pdf, pagina_num)

    pdf.showPage()
    pdf.save()

    return response

def logout_view(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'POST':
     form= RegistroForm(request.POST)
     if form.is_valid():
         form.save()
         return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})


