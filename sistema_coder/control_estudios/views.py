"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render


   

def lista_estudiantes (request):
    contexto = {
        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Dautel"},
            {"nombre": "Manuela", "apellido": "Gomez"},
            {"nombre": "Ivan", "apellido": "Tomasevich"},
            {"nombre": "Carlos", "apellido": "Perez"},
        ]
     }
    http_responde=render(
        request = request,
        template_name= 'control_estudios/lista_estudiantes.html',
        context = contexto,
    )
    return http_responde

def lista_cursos (request):
    contexto = {
        "cursos": [
            {"nombre": "Phyton", "comision": "33245"},
            {"nombre": "FrontEnd", "comision": "55698"},
            {"nombre": "SQL", "comision": "45887"},
        ]
     }
    http_responde=render(
        request = request,
        template_name= 'control_estudios/lista_cursos.html',
        context = contexto,
    )
    return http_responde

