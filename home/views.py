from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact,Task
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from home.forms import CreateTaskForm,CreateUserForm,LoginForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    '''
    context = {
        "variable": "this is variable"
    }
    variable value is = <b>{{variable}}</b>
    '''
    return render(request,"index.html")
    #return HttpResponse("This is home page")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        usertype = request.POST.get('usertype')
        contact = Contact(name = name,email = email ,phone = phone ,desc = desc ,date = datetime.today(),usertype = usertype)
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, "contact.html")


def pricing(request):
    return render(request, "pricing.html")

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password') 
            user = authenticate(request,username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("logged")
    context = {'form' : form}
    return render(request, "login.html",context=context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def forgot(request):
    return render(request, "forgot.html")

@login_required(login_url='login')
def logged(request):
    return render(request, "profile/logged.html")

def register(request):
    form = CreateUserForm()
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("logged")
    context = {'form': form}
    return render(request, "register.html",context = context)


@login_required(login_url='login')
def createtask(request):
    form = CreateTaskForm()
    form.fields['posted'].widget.attrs['readonly'] = True
    form.fields['late'].widget.attrs['readonly'] = True
    if request.method == 'POST' :
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('viewtask')
    context = {'form': form}
    return render(request, "profile/createtask.html", context=context)



@login_required(login_url='login')
def viewtask(request):
    current_user = request.user.id
    task1 = Task.objects.all().filter(user=current_user)
    context = {'task1': task1}
    for t in task1:
        if ((timezone.now()>t.deadline) and (t.completion == 'Not Done')):
            t.late = 'Late'
    return render(request, "profile/viewtask.html", context=context)


@login_required(login_url='login')
def updatetask(request,pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)
    form.fields['posted'].widget.attrs['readonly'] = True
    form.fields['late'].widget.attrs['readonly'] = True
    form.fields['title'].widget.attrs['readonly'] = True
    form.fields['content'].widget.attrs['readonly'] = True
    form.fields['deadline'].widget.attrs['readonly'] = True
    if request.method == 'POST':
        form = CreateTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('viewtask')
    context = {'form': form}
    return render(request, "profile/updatetask.html", context=context)


@login_required(login_url='login')
def deletetask(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('viewtask')
    context = { 'object' : task}
    return render(request, "profile/deletetask.html", context=context)
