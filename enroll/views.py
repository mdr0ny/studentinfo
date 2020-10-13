from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import StudentRegistration
from .models import User 

# Create your views here.
#This Function Will add new item and show items 
def index(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg = User(name=name,email=email,password=password)
            reg.save()
            form = StudentRegistration()
    else:
         form = StudentRegistration()
    stud = User.objects.all()


    return render(request,'index.html',{'form':form,'stu':stud})
#This function will update
def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
    return render(request,'update.html',{'form':form})


#this function will delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
