from django.shortcuts import render
from .models import ExampleModel
from django.http import Http404


# Create your views here.
def example_view(request,id):
      try:
            example=ExampleModel.objects.get(id=id)
      except ExampleModel.DoesNotExist:
            raise Http404("ExampleModel with the given ID does not exist.")
      return render(request, 'example.html', {'id': id, 'example': example})