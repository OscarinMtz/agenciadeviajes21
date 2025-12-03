
from django import forms
from .models import (
    Vuelo, Alojamiento, Paquete_Turistico, Cliente_Viajes, 
    Agente_Viajes, Reserva_Viaje, Destino
)

class DatePreservingModelForm(forms.ModelForm):
    """
    Este ModelForm personalizado evita que los campos de fecha se borren durante la actualización.
    Si un campo de fecha se envía vacío, conservará su valor original.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hace que todos los campos de fecha no sean obligatorios en el formulario.
        for field in self.fields.values():
            if isinstance(field, forms.DateField):
                field.required = False

    def clean(self):
        cleaned_data = super().clean()
        # Si se está actualizando una instancia y un campo de fecha está vacío, restaura el valor original.
        if self.instance and self.instance.pk:
            for field_name, field in self.fields.items():
                if isinstance(field, forms.DateField) and not cleaned_data.get(field_name):
                    cleaned_data[field_name] = getattr(self.instance, field_name)
        return cleaned_data

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class VueloForm(DatePreservingModelForm):
    class Meta:
        model = Vuelo
        fields = '__all__'
        widgets = {
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
            'fecha_llegada': forms.DateInput(attrs={'type': 'date'}),
        }

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = '__all__'

class PaqueteForm(DatePreservingModelForm):
    vuelos = forms.ModelMultipleChoiceField(
        queryset=Vuelo.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    alojamientos = forms.ModelMultipleChoiceField(
        queryset=Alojamiento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Paquete_Turistico
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class ClienteForm(DatePreservingModelForm):
    class Meta:
        model = Cliente_Viajes
        fields = '__all__'
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

class AgenteForm(DatePreservingModelForm):
    class Meta:
        model = Agente_Viajes
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

class ReservaForm(DatePreservingModelForm):
    class Meta:
        model = Reserva_Viaje
        fields = '__all__'
        widgets = {
            'fecha_vencimiento_pago': forms.DateInput(attrs={'type': 'date'}),
        }
