from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.db import IntegrityError
from personas.models import Personas
def hola(request):
  
  return HttpResponse("<h1>Hola estimados alumnos de UNEWEB </h1>")

def otro_hola(request):
  CONTENIDO_HTML= """
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Otro Saludo</title>
  <style>
    h1{
      text-align: center;
      padding: 20px;
      background-color: #ccc;
      color: blue;
      border-radius: 25px;
      border-style: solid;
      border-width: 2px;
      border-color: purple;
      font-family: Arial, Helvetica, sans-serif;
      margin-top: 20px;
    }
    </style>
</head>
<body>
  <h1>hola este es otro saludo,para los estudiante de Uneweb</h1>
  
</body>
</html>

  """
  return HttpResponse(CONTENIDO_HTML)

def obtener_fecha_hora(request):
  ahora = datetime.datetime.now() 
  mostrar_ahora = "<h2>" + str(ahora) +"</h2>"
  return HttpResponse(mostrar_ahora)

def inicio(request):
  return render(request,"index.html")

def ingresar(request):
    return render(request, 'ingresar.html')

def ingresar01(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            #Obtener datos del formulario
            vced = request.POST.get('cedula')
            vnom = request.POST.get('nombre')
            vape = request.POST.get('apellido')
            vtel = request.POST.get('telefono')
            vdir = request.POST.get('direccion')
            vcor = request.POST.get('correo')
            vfna = request.POST.get('fecha_nacimiento')
            # Se crea el objeto a partir de la clase Persona
            persona_tmp = Personas(cedula=vced, nombre=vnom, apellido=vape, telefono=vtel,direccion=vdir, correo=vcor, fecha_nacimiento=vfna)
            # Guardar en BBDD
            persona_tmp.save()
            # Se genera el mensaje informativo de aprobación
            mensaje = 'El registro fue almacenado con éxito'
        except IntegrityError as e:
            # Se genera el mensaje informativo de error
            mensaje = 'Error: El registro no pudo ser almacenado'
        return render(request, 'ingresar.html',{'mensaje':mensaje})
