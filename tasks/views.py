from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required;
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
from datetime import datetime
from .models import Task

@login_required #requerindo o login nas views
def taskList(request):
  search = request.GET.get('search') #search irá receber o parametro de get do front
  filter = request.GET.get('filter')
  tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user = request.user).count()
  tasksDone = Task.objects.filter(done='done', user=request.user).count()
  tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

  if search:
    tasks = Task.objects.filter(title__icontains = search, user=request.user) #irá fazer o filtro pelo titulo da tarefa
  elif filter:
    tasks = Task.objects.filter(done = filter, user=request.user)
    import datetime
  else:

    tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user) #a variavel irá atribuir todos os objetos da task do BD

    #As proximas 3 linhas são responsaveis pela paginação do site
    paginator = Paginator(tasks_list, 3) #O primeiro argumento é referente a variavel com a lista de objetos e a segunda do numero de publicações por pagina
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

  return render(request, 'tasks/list.html', 
    {'tasks': tasks,'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing})

@login_required
def taskView(request, id):
  task = get_object_or_404(Task, pk=id) #Esse metodo precisa de dois argumentos: Model, e o ID
  return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid(): #verifica se o formulário é válido
      task = form.save(commit = False) #o commit faz parar o processo de salvar
      task.done = 'doing' #altera o status de done para doing
      task.user = request.user #filtro para adicionar tarefas somente no usuario logado
      task.save() #salva o task
      
      messages.info(request, 'Tarefa salva com sucesso.')

      return redirect('/') #redireciona apos clicar em salvar para a raiz "/"

  else:
    form = TaskForm()
    return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
  task = get_object_or_404(Task, pk=id)
  form = TaskForm(instance=task)

  if (request.method == 'POST'):
    form = TaskForm(request.POST, instance=task)
    if (form.is_valid()):
      task.save()

      messages.info(request, 'Tarefa editada com sucesso.')
  
      return redirect ("/")
    else:
      return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
  else:
    return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def deleteTask(request, id):
  task = get_object_or_404(Task, pk=id)
  task.delete()

  messages.info(request, 'Tarefa deletada com sucesso.')

  return redirect('/')
@login_required
def changeStatus(request,id):
  task = get_object_or_404(Task, pk=id)
  if(task.done == 'doing'):
    task.done = 'done'
  else:
    task.done = 'doing'

  task.save()

  return redirect('/')
def helloworld(request):
  return HttpResponse('Hello World')

def yourName(request, name):
  return render(request, 'tasks/yourname.html', {'name': name})
