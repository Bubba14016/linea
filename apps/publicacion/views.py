from django.shortcuts import render
from django.views.generic import ListView
from apps.publicacion.models import publicacion
# Create your views here.

class Listar(ListView):
	model= publicacion
	template_name='base.html'

	