from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Car,Manufacturer
# Create your views here.

class ManufacturerList(ListView):
    model = Manufacturer 
    template_name: str = "work2/manufacturer_list.html"
    context_object_name = "manufacturers"



