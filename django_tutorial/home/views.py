from django.shortcuts import render
from django.http import HttpResponse


from .models import departments,doctors

def index(request):

    person = {
        'name':'johan',
        'age':34,
        'place':'calicut'
    }
    return render(request,'index.html',person)


def about(request):
    number ={
        'num':13,
    }
    return render(request,'about.html',number)


def booking(request):
    number2={
        'token':[1,2,3,4,5,6,7,8,9]
    }
    return render(request,'booking.html',number2)


def doctors(request):
    dict_docs = {
        'doctors': doctors.objects.all()
        }
    return render(request,'doctors.html',dict_docs)


def contact(request):
    return render(request,'contact.html')


def department(request):
    dict_dept ={
        'dept': departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
