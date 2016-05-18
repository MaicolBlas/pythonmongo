from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Planilla
from django.http import HttpResponseRedirect

def planillas(request):
	planillas = Planilla.objects()
	template = loader.get_template('index.html')
	context = {
	 	'planillas': planillas
	}

	return HttpResponse(template.render(context, request))


def registrar(request):
	if request.method == 'POST':
		planilla = Planilla(idTrabajador=request.POST['idTrabajador'], apellidos=request.POST['apellidos'], nombres=request.POST['nombres'], direccion=request.POST['direccion'], estado=request.POST.get('estado', False))
		planilla.save()
		return HttpResponseRedirect('/')

	template = loader.get_template('registrar.html')
	context = {
	}

	return HttpResponse(template.render(context, request))	
