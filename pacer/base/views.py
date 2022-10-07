from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Tarea

class TaskList(ListView):
    model = Tarea
