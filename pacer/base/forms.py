from django import forms

#reorganizando los formularios y las vistas


class PositionForm(forms.Form):
    position = forms.CharField()