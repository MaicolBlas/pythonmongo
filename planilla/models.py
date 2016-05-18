from __future__ import unicode_literals
from django.db import models

# Create your models here.
from mongoengine import *

class Planilla(Document):
	idTrabajador = IntField()
	apellidos = StringField(max_length=200)
	nombres = StringField(max_length=200)
	direccion = StringField(max_length=200)
	estado = BooleanField()
