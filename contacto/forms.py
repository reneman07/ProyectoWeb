from django import forms


class FormulatioContacto(forms.Form):
    #your_name = forms.CharField(label="Your name", max_length=100)
    nombre = forms.CharField(label = "Nombre", required = True, max_length = 50)
    email = forms.EmailField(label = "Email", required = True)
    contenido = forms.CharField(label = "Contenido", widget = forms.Textarea, required = False)

    