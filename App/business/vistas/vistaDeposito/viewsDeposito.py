from contextlib import redirect_stderr
from email.mime import audio
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from ps.conexion import *
from xhtml2pdf import pisa
from django.template.loader import get_template

##LOGIN
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import logout

### ZONA DEPÓSITO

@login_required
def deposito(request):
    variable = "deposito"
    return render(request,'business/deposito/deposito.html', {'business': variable, 'deposito': variable})
