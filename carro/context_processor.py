from django.http import HttpResponse
from django.template import RequestContext, Template
import traceback

def importe_total_carro(request):
    total = 0
    """for key, value in request.session['carro'].items():
                total = total + float(value["precio"])"""
    if request.user.is_authenticated:
        try:
            for key, value in request.session['carro'].items():
                total = total + float(value["precio"])
        except Exception as e:
            print("======== Here {}".format(e))
            traceback.print_exc()
    else:
        total = "Debes loguearte"

    return {"importe_total_carro": total}