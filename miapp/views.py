from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib import messages
from miapp.forms import FormRegion
from miapp.models import Region
from miapp.forms import FormEmpleado
from miapp.models import Employee

# Create your views here.
layout = """
    <h1> Exámen Final (LP3) || </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
      
    return render(request, 'index.html', {
        'titulo': 'Inicio',
    })

def listar_empleado(request):
    employees = Employee.objects.all()
    """
    employees = Employee.objects.filter(
        Q(nombre__contains="Py") |
        Q(nombre__contains="Hab")
    )
    """
    return render(request, 'listar_empleado.html',{
        'employees': employees,
        'titulo': 'Listado de Empleados'
    })

def eliminar_empleado(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('listar_empleado')

def save_empleado(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        if len(fullname)<=2:
            return HttpResponse("<h2>El tamaño del nombre es pequeño, intente nuevamente</h2>")
        job = request.POST['job']
        estado = request.POST['estado']

        employee = Employee(
            fullname = fullname,
            job= job,
            estado = estado
        )
        employee.save()
        return HttpResponse(f"Empleadocreada: {employee.fullname} ")
    else:
        return HttpResponse("<h2> No se ha podido registrar la region</h2>")

def create_full_empleado(request):
    if request.method == 'POST':
        formulario1 = FormRegion(request.POST)
        if formulario1.is_valid():
            data_form = formulario1.cleaned_data
            fullname = data_form['fullname']
            job = data_form['job']
            estado = data_form['estado']

            employee = Employee(
                fullname = fullname,
                job = job,
                estado = estado
            )
            employee.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se registró correctamente al empleado {employee.id}')

            return redirect('listar_empleado')
    else:
        formulario1 = FormEmpleado()        
    return render(request, 'create_full_empleado.html',{
        'form': formulario1
    })


def listar_region(request):
    regiones = Region.objects.all()
    """
    regiones = Region.objects.filter(
        Q(nombre__contains="Py") |
        Q(nombre__contains="Hab")
    )
    """
    return render(request, 'listar_region.html',{
        'regiones': regiones,
        'titulo': 'Listado de Regiones'
    })

def eliminar_region(request, id):
    region = Region.objects.get(pk=id)
    region.delete()
    return redirect('listar_region')

def save_region(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(name)<=2:
            return HttpResponse("<h2>El tamaño del nombre es pequeño, intente nuevamente</h2>")
        cases = request.POST['cases']
        deaths = request.POST['deaths']
        lethality = request.POST['lethality']

        region = Region(
            name = name,
            cases = cases,
            deaths = deaths,
            lethality = lethality
        )
        region.save()
        return HttpResponse(f"Region creada: {region.name} ")
    else:
        return HttpResponse("<h2> No se ha podido registrar la region</h2>")

def create_full_region(request):
    if request.method == 'POST':
        formulario2 = FormRegion(request.POST)
        if formulario2.is_valid():
            data_form = formulario2.cleaned_data
            name = data_form['name']
            cases= data_form['cases']
            deaths = data_form['deaths']
            lethality = data_form['lethality']
            region = Region(
                name = name,
                cases = cases,
                deaths = deaths,
                lethality = lethality
            )
            region.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se registró correctamente la carrera {region.id}')

            return redirect('listar_region')
    else:
        formulario2 = FormRegion()        
    return render(request, 'create_full_region.html',{
        'form': formulario2
    })
