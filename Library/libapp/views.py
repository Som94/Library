from django.shortcuts import render,redirect
from libapp.models import LibraryModel
from libapp.forms import LibraryForm
from libapp.forms1 import SignUpForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
import time

# Create your views here.
def Home_view(request):
    return render(request,'html/home.html')

@login_required()
def Retrive_view(request):
    list=LibraryModel.objects.all()
    return render(request, 'html/list.html',{'list':list})

@login_required()
def Insert_view(request):
    form=LibraryForm()
    if request.method=='POST':
        form=LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'html/insert.html',{'form':form})

@login_required()
def Delete_view(request,id):
    book=LibraryModel.objects.get(id=id)
    book.delete()
    return redirect('/')

@login_required
def Update_view(request,id):
    book=LibraryModel.objects.get(id=id)
    if request.method=='POST':
        form=LibraryForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'html/update.html',{'book':book})

def Logout_view(request):
    return render(request,'html/logout.html')


def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')
    return render(request,'html/signup.html',{'form':form})
