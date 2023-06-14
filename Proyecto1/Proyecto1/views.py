from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("Que haces pa?")

def seg_vista(request):
    return HttpResponse("<br><br><h1>Todo bien?</h1>")

def miNombreEs(self, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"

def probandoTemplates(self):
    nombre = "Matias"
    apellido = "Pazos"
    namelist = ["Matias", "Lucas", "Martina", "Simon", "Victor"]

    diccionario = {

        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist,
    }

    plantilla = loader.get_template("home.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

