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

### ZONA CARGAS

@login_required
def cargas(request):
    variable = "cargas"
    return render(request,'business/cargas/cargas.html', {'business': variable, 'cargas': variable})
