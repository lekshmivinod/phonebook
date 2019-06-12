
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


# def hello(request):
#    today = datetime.datetime.now().date()
#    return HttpResponse(today)


from django.shortcuts import redirect


from .models import wrongnumber
def index(request):
   members=wrongnumber.objects.all()
   context={"members" :members}
   return render (request,'crud/index.html',context)
def create(request):
   member=wrongnumber(Firstname=request.POST['Firstname'],Lastname=request.POST['Lastname'],Phonenumber=request.POST['Phonenumber'])
   member.save()
   return redirect('/')

def edit(request,id):
    member=wrongnumber.objects.get(id=id)
    context={'members':member}
    return render(request,'crud/edit.html',context)

def update(request,id):
    member=wrongnumber.objects.get(id=id)
    member.Firstname=request.POST['Firstname']
    member.Lastname=request.POST['Lastname']
    member.Lastname=request.POST['Phonenumber']

    member.save()
    return redirect('/')

def delete (request,id):
    member=wrongnumber.objects.get(id=id)
    member.delete()
    return redirect('/')


