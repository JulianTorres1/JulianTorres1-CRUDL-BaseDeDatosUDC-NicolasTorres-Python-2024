from django.shortcuts import render, redirect
from .models import Vehiculo


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Vehiculo
# Create your views here.

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    vehiculos_ordenados = Vehiculo.objects.order_by('precio')
    return render(request, 'list_vehiculos.html', {
        "vehiculos": vehiculos,
        "vehiculos_ordenados": vehiculos_ordenados
    })
def create_vehiculo(request):
    en_stock = request.POST.get('en_stock') == 'on'
    vehiculo = Vehiculo(
        num_bastidor=request.POST['num_bastidor'],
        nombre_modelo=request.POST['nombre_modelo'],
        precio=request.POST['precio'],
        descuento=request.POST['descuento'],
        potencia_fiscal=request.POST['potencia_fiscal'],
        cilindrada=request.POST['cilindrada'],
        en_stock=en_stock,
        id_concesionario=request.POST['id_concesionario'],
        id_servicio=request.POST['id_servicio']
    )
    vehiculo.save()
    return redirect('/vehiculos/')

def delete_vehiculo(request, num_bastidor):
    vehiculo = Vehiculo.objects.get(num_bastidor=num_bastidor)
    vehiculo.delete()
    return redirect('/vehiculos/')

def edit_vehiculo(request, num_bastidor):
    vehiculo = get_object_or_404(Vehiculo, num_bastidor=num_bastidor)
    if request.method == 'POST':
        try:
            vehiculo.nombre_modelo = request.POST['nombre_modelo']
            vehiculo.precio = request.POST['precio']
            vehiculo.descuento = request.POST['descuento']
            vehiculo.potencia_fiscal = request.POST['potencia_fiscal']
            vehiculo.cilindrada = request.POST['cilindrada']
            vehiculo.en_stock = request.POST.get('en_stock') == 'on'
            vehiculo.id_concesionario = request.POST['id_concesionario']
            vehiculo.id_servicio = request.POST['id_servicio']
            vehiculo.save()
            return redirect('/vehiculos/')
        except KeyError as e:
            return HttpResponseBadRequest(f"Missing field: {e}")
    else:
        return render(request, 'edit_vehiculo.html', {"vehiculo": vehiculo})