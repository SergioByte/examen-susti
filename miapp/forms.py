from django import forms
from django.core import validators

class FormRegion(forms.Form):
    name = forms.CharField(
        label="NOMBRE",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el nombre de la region',
                'class': 'nombre_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(2,'El nombre es corto'),
            validators.MaxLengthValidator(20,'Superaste el límite de caracteres')
        ]
    )
    cases = forms.CharField(
        label="CASOS",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese la cantidad de casos PCR(+)',
                'class': 'cases_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(0,'Ingrese cantidad valida'),
            validators.MaxLengthValidator(5,'Ingrese cantidad valida')
        ]
    )
    deaths = forms.CharField(
        label="MUERTES",
        max_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese la cantidad de muertes',
                'class': 'deaths_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(0,'Ingrese cantidad valida'),
            validators.MaxLengthValidator(5,'Ingrese cantidad valida')
        ]
    )

    lethality = forms.CharField(
        label="LETALIDAD",
        max_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el porcentaje de letalidad',
                'class': 'lethality_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(0,'Ingrese porcentaje valido'),
            validators.MaxLengthValidator(4,'Ingrese porcentaje valido')
        ]
    )

