from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

'''def home(requests):
    page=loader.get_template("comment.html")
    context={"Email":result.Email,"Password":result.Password}
    return HttpResponse(page.render(context))
    result=user.objects.filter(Id=1).first()
    #return HttpResponse("<h2>خوش آمدید به اولین پروژه </h2>")

def comment(requests):
        return render(request=request , template_name="comment.html",context={})

def data(requests):
        user= models.user(Email="leila.elham.51@gmail.com",Password="60612")
        user.save()
        return render(request=request, template_name="form.html", context={"form"=form1})

def datatable(requests):
       alldata=models.user.abjects.all()
        return render(request=request, template_name="datatable.html", context={'alldata':alldata}
from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
     return render(request=request, template_name='comment.html',context={})


def data(request):

     form1=()
     return render(request=request, template_name='formtest.html',context={'form':form1})


def datatable(request):
     alldata=models.User.objects.all()
     return render(request=request, template_name='datatable.html',context={'alldata':alldata})

def saveData(request):
     if request.method=='POST':
          form2=(request.POST)
          data=models.User(Email=form2.data['Email'],Password=form2.data['Password'])
          data.save()
          alldata = models.User.objects.all()
          return render(request=request,template_name='datatable.html',context={'alldata':alldata})'''
from django.shortcuts import render
from . import models
from .import form
# Create your views here.
def comment(request):
     form1 = form.userForm()
     return render(request=request, template_name='formtest.html',context={'form':form1})


def data(request):
     user=models.User(Email="adibradp@gmail.com",Password="poo123456789")
     user.save()
     return render(request=request, template_name='data.html',context={})


def datatable(request):
     alldata=models.User.objects.all()
     return render(request=request, template_name='datatable.html',context={'alldata':alldata})

def SaveData(request):
     if request.method=="post":
          form2=form.userForm(request.post)
          data=models.User(Email=form2.data['Email'],Password=form2.data['Password'])
          data.save()
          alldata = models.User.objects.all()
          return render(request=request, template_name='saveData.html',context={'alldata':alldata})





