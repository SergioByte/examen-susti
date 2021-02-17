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

class FormEmpleado(forms.Form):

    fullname = forms.CharField(
        label="Nombre completo",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el nombre completo',
                'class': 'fullname_form_empleados'
            }
        ),
        validators=[
            validators.MinLengthValidator(2,'El nombre es corto'),
            validators.MaxLengthValidator(50,'Superaste el límite de caracteres')
        ]
    )
    job = forms.CharField(
        label="Cargo",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese la labor que desempeña',
                'class': 'job_form_empleados'
            }
        ),
        validators=[
            validators.MinLengthValidator(2,'El nombre es corto'),
            validators.MaxLengthValidator(30,'Superaste el límite de caracteres')
        ]
    )

    opciones_estado = [
        (1,'A'),
        (0,'B'),
    ]
    estado = forms.TypedChoiceField(
        label="ESTADO",
        choices=opciones_estado
    )

