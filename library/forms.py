from django import forms

class FormularioContactos(forms.Form):
    asunto = forms.CharField(min_length=5, max_length=50)
    email = forms.EmailField(required=False, label='E-mail')
    mensaje = forms.CharField(widget=forms.Textarea, min_length=10, max_length=500)

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("¡Se requieren minimo 4 palabras!")
        return mensaje