from django.shortcuts import render
from todos.models import Tasks

# Create your views here.
def todo_view(request):
      completed_tasks = Tasks.objects.filter(is_completed=True)
      pending_tasks = Tasks.objects.filter(is_completed=False)

      context={
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks
      }

      return render(request,'todo.html',context)
