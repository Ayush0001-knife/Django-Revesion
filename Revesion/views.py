from django.http import HttpResponse
from django.shortcuts import render
from data.models import ExampleModel

def home(request):
      example = ExampleModel.objects.all()
      context = {
            'example': example
      }
      return render(request,'home.html',context)