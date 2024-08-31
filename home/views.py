from django.shortcuts import render,redirect
from .models import TODO
from .forms import CreateTodoForms,UpdateTodoForm
from django.contrib import messages
# from django.contrib import messages




# Create your views here.

def home(request):
    todo=TODO.objects.all
    return render(request,'home.html',{'all':todo})

def detail(request,todo_id):
    todo=TODO.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})

def create(request):
    if (request.method =="POST"):
        form=CreateTodoForms(request.POST)
        if form.is_valid() :
            cd=form.cleaned_data
            TODO.objects.create(title=cd['title'],body=cd['body'],created=cd['created'])
            msg='Todo \''+ cd['title']+ '\' Create Successfully'
            messages.success(request,msg,'success')
            return redirect('home')
    else:
        form=CreateTodoForms()
    
    return render(request,'create.html',{'form':form})

        
def delete(request,todo_id):
    todo=TODO.objects.get(id=todo_id)
    TODO.objects.get(id=todo_id).delete()
    msg='Todo \''+todo.title+'\' delete Successfully'
    messages.success(request,msg,'success')
    return redirect('home')


def update(request,todo_id):
    todo=TODO.objects.get(id=todo_id)

    if request.method=='POST':
        form=UpdateTodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Update done!','success')
            # return redirect('home')
            return redirect('details',todo_id)

    else:
        form=UpdateTodoForm(instance=todo)

    return render (request,'update.html',{'form':form})
    









