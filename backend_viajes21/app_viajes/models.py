
from django.db import models

class Destino(models.Model):
    id_destino = models.AutoField(primary_key=True)
    nombre_destino = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    continente = models.CharField(max_length=50)
    descripcion = models.TextField()
    atracciones_principales = models.TextField()
    clima = models.CharField(max_length=50)
    divisa_local = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre_destino}, {self.pais}"

class Vuelo(models.Model):
    id_vuelo = models.AutoField(primary_key=True)
    num_vuelo = models.CharField(max_length=20)
    aerolinea = models.CharField(max_length=100)
    origen = models.ForeignKey(Destino, related_name='vuelos_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, related_name='vuelos_destino', on_delete=models.CASCADE)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    fecha_llegada = models.DateField()
    hora_llegada = models.TimeField()
    precio_clase_economica = models.DecimalField(max_digits=10, decimal_places=2)
    asientos_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.num_vuelo}: {self.origen.nombre_destino} -> {self.destino.nombre_destino}"

class Alojamiento(models.Model):
    id_alojamiento = models.AutoField(primary_key=True)
    nombre_hotel = models.CharField(max_length=255)
    tipo_alojamiento = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, null=True, blank=True)
    estrellas = models.IntegerField()
    precio_noche_estandar = models.DecimalField(max_digits=10, decimal_places=2)
    servicios_incluidos = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_hotel} en {self.destino.nombre_destino if self.destino else 'Destino no especificado'}"

class Paquete_Turistico(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    nombre_paquete = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    vuelos = models.ManyToManyField(Vuelo, blank=True, related_name='paquetes')
    alojamientos = models.ManyToManyField(Alojamiento, blank=True, related_name='paquetes')
    precio_adulto = models.DecimalField(max_digits=10, decimal_places=2)
    precio_nino = models.DecimalField(max_digits=10, decimal_places=2)
    cupo_maximo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_paquete} ({self.id_destino.nombre_destino})"

class Cliente_Viajes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateField()
    preferencias_viaje = models.TextField()
    pasaporte = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Agente_Viajes(models.Model):
    id_agente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Reserva_Viaje(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_paquete = models.ForeignKey(Paquete_Turistico, on_delete=models.CASCADE, null=True, blank=True)
    id_vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, null=True, blank=True)
    id_alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE, null=True, blank=True)
    id_cliente = models.ForeignKey(Cliente_Viajes, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    num_adultos = models.IntegerField()
    num_ninos = models.IntegerField()
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    estado_reserva = models.CharField(max_length=50)
    fecha_vencimiento_pago = models.DateField()
    id_agente_venta = models.ForeignKey(Agente_Viajes, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.id_paquete:
            return f"Reserva de {self.id_cliente} para el paquete {self.id_paquete.nombre_paquete}"
        
        vuelo_info = f"vuelo {self.id_vuelo.num_vuelo}" if self.id_vuelo else "ningún vuelo"
        alojamiento_info = f"alojamiento en {self.id_alojamiento.nombre_hotel}" if self.id_alojamiento else "ningún alojamiento"
        return f"Reserva de {self.id_cliente} para {vuelo_info} y {alojamiento_info}"
