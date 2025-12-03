from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Destino, Paquete_Turistico, Cliente_Viajes, Reserva_Viaje, 
    Vuelo, Alojamiento, Agente_Viajes
)
from .forms import (
    DestinoForm, PaqueteForm, ClienteForm, ReservaForm,
    VueloForm, AlojamientoForm, AgenteForm
)

def index(request):
    return render(request, 'index.html')

# Vistas para Vuelos
def vuelo_list(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'vuelo_list.html', {'vuelos': vuelos})

def vuelo_create(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vuelo_list')
    else:
        form = VueloForm()
    return render(request, 'vuelo_form.html', {'form': form, 'title': 'Añadir Vuelo'})

def vuelo_update(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    if request.method == 'POST':
        form = VueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('vuelo_list')
    else:
        form = VueloForm(instance=vuelo)
    return render(request, 'vuelo_form.html', {'form': form, 'title': 'Editar Vuelo'})

def vuelo_delete(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    if request.method == 'POST':
        vuelo.delete()
        return redirect('vuelo_list')
    return render(request, 'confirm_delete.html', {'object': vuelo})

# Vistas para Alojamientos
def alojamiento_list(request):
    alojamientos = Alojamiento.objects.all()
    return render(request, 'alojamiento_list.html', {'alojamientos': alojamientos})

def alojamiento_create(request):
    if request.method == 'POST':
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alojamiento_list')
    else:
        form = AlojamientoForm()
    return render(request, 'alojamiento_form.html', {'form': form, 'title': 'Añadir Alojamiento'})

def alojamiento_update(request, pk):
    alojamiento = get_object_or_404(Alojamiento, pk=pk)
    if request.method == 'POST':
        form = AlojamientoForm(request.POST, instance=alojamiento)
        if form.is_valid():
            form.save()
            return redirect('alojamiento_list')
    else:
        form = AlojamientoForm(instance=alojamiento)
    return render(request, 'alojamiento_form.html', {'form': form, 'title': 'Editar Alojamiento'})

def alojamiento_delete(request, pk):
    alojamiento = get_object_or_404(Alojamiento, pk=pk)
    if request.method == 'POST':
        alojamiento.delete()
        return redirect('alojamiento_list')
    return render(request, 'confirm_delete.html', {'object': alojamiento})

# Vistas para Agentes
def agente_list(request):
    agentes = Agente_Viajes.objects.all()
    return render(request, 'agente_list.html', {'agentes': agentes})

def agente_create(request):
    if request.method == 'POST':
        form = AgenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agente_list')
    else:
        form = AgenteForm()
    return render(request, 'agente_form.html', {'form': form, 'title': 'Añadir Agente'})

def agente_update(request, pk):
    agente = get_object_or_404(Agente_Viajes, pk=pk)
    if request.method == 'POST':
        form = AgenteForm(request.POST, instance=agente)
        if form.is_valid():
            form.save()
            return redirect('agente_list')
    else:
        form = AgenteForm(instance=agente)
    return render(request, 'agente_form.html', {'form': form, 'title': 'Editar Agente'})

def agente_delete(request, pk):
    agente = get_object_or_404(Agente_Viajes, pk=pk)
    if request.method == 'POST':
        agente.delete()
        return redirect('agente_list')
    return render(request, 'confirm_delete.html', {'object': agente})

# Vistas para Destinos
def destino_list(request):
    destinos = Destino.objects.all()
    return render(request, 'destino_list.html', {'destinos': destinos})

def destino_create(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destino_list')
    else:
        form = DestinoForm()
    return render(request, 'destino_form.html', {'form': form, 'title': 'Añadir Destino'})

def destino_update(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if request.method == 'POST':
        form = DestinoForm(request.POST, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('destino_list')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'destino_form.html', {'form': form, 'title': 'Editar Destino'})

def destino_delete(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if request.method == 'POST':
        destino.delete()
        return redirect('destino_list')
    return render(request, 'confirm_delete.html', {'object': destino})

# Vistas para Paquetes
def paquete_list(request):
    paquetes = Paquete_Turistico.objects.select_related('id_destino').all()
    return render(request, 'paquete_list.html', {'paquetes': paquetes})

def paquete_create(request):
    if request.method == 'POST':
        form = PaqueteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paquete_list')
    else:
        form = PaqueteForm()
    return render(request, 'paquete_form.html', {'form': form, 'title': 'Añadir Paquete'})

def paquete_update(request, pk):
    paquete = get_object_or_404(Paquete_Turistico, pk=pk)
    if request.method == 'POST':
        form = PaqueteForm(request.POST, instance=paquete)
        if form.is_valid():
            form.save()
            return redirect('paquete_list')
    else:
        form = PaqueteForm(instance=paquete)
    return render(request, 'paquete_form.html', {'form': form, 'title': 'Editar Paquete'})

def paquete_delete(request, pk):
    paquete = get_object_or_404(Paquete_Turistico, pk=pk)
    if request.method == 'POST':
        paquete.delete()
        return redirect('paquete_list')
    return render(request, 'confirm_delete.html', {'object': paquete})

# Vistas para Clientes
def cliente_list(request):
    clientes = Cliente_Viajes.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form, 'title': 'Añadir Cliente'})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente_Viajes, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form, 'title': 'Editar Cliente'})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente_Viajes, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'confirm_delete.html', {'object': cliente})

# Vistas para Reservas
def reserva_list(request):
    reservas = Reserva_Viaje.objects.select_related('id_vuelo', 'id_alojamiento', 'id_cliente').all()
    return render(request, 'reserva_list.html', {'reservas': reservas})

def reserva_create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm()
    return render(request, 'reserva_form.html', {'form': form, 'title': 'Añadir Reserva'})

def reserva_update(request, pk):
    reserva = get_object_or_404(Reserva_Viaje, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reserva_form.html', {'form': form, 'title': 'Editar Reserva'})

def reserva_delete(request, pk):
    reserva = get_object_or_404(Reserva_Viaje, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva_list')
    return render(request, 'confirm_delete.html', {'object': reserva})