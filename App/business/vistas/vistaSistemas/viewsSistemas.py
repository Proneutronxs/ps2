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


### ZONA SISTEMAS

@login_required
def sistemas(request):
    variable = "sistemas"
    return render(request,'business/sistemas/sistemas.html', {'business': variable, 'sistemas': variable})