from django.shortcuts import render, redirect
from .forms import FormulatioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    if request.method == "POST":
        formulario_contacto = FormulatioContacto(data = request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido") + " " + email
            mail = EmailMessage("Mensaje enviado por " + nombre, "El usuario {} con la direccion {} escribe lo siguiente:\n\n{} ".format(nombre, email, contenido), email, ["rene_mansilla@yahoo.com"], reply_to = [email])
            try:
                mail.send()
                return redirect("/contacto/?valido")
            except:
                print("error al enviar")
                return redirect("/contacto/?invalido")
    else:
        formulario_contacto = FormulatioContacto()

    return render(request, "contacto/contacto.html", {"miFormulario": formulario_contacto})

