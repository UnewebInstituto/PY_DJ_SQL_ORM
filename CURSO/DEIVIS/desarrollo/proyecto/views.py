from django.http import HttpResponse
import datetime
from django.shortcuts import render
def hola(request):
    return HttpResponse("<h1> Hola estimados alumnos de UNEWEB<h1>")

def otro_hola(request):
    CONTENIDO_HTML ="""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Otro Saludo</title>
  <style>
      h1{
        text-align: center;
        padding: 20px;
        background-color: rgb(195, 195, 195);
        color: blue;
        border-radius: 25px;
        border-style: solid;
        border-width: 2px;
        border-color: brown;
        font-family: arial;
        margin-top: 20px;
      }
  </style>
</head>
<body>
  <h1>Hola este es otro saludo para los estudiantes de Uneweb</h1>
</body>
</html>
    """
    return HttpResponse(CONTENIDO_HTML)


def obtener_fecha_hora(request):
    ahora= datetime.datetime.now()
    mostrar_ahora = "<h2>"+ str(ahora) + "</h2>"
    return HttpResponse(mostrar_ahora)


def inicio(request):
    print("se ejecuto inicio")
    return render(request, 'index.html')

def ingresar(request):
    print("se ejecuto inicio")
    return render(request, 'ingresar.html')