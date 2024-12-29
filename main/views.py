from django.shortcuts import render, redirect
from .models import Member

def index (request):
    mem = Member.objects.all()
    return render(request, 'main/index.html', {"mem":mem});

def  add(request):
    return render(request, 'main/add.html')

def addrec(request):
    a = request.POST['lastname']
    b = request.POST['firstname']
    c = request.POST['post']
    d = request.POST['date']
    e = request.POST['email']
    f = request.POST['number']
    g = request.POST['status']
    mem = Member(lastname=a,firstname=b,post=c,data=d,email=e,number=f,status=g)
    mem.save()
    return redirect("/")

def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'main/update.html',{'mem':mem})

def uprec(request, id):
    a = request.POST['lastname']
    b = request.POST['firstname']
    c = request.POST['post']
    d = request.POST['date']
    e = request.POST['email']
    f = request.POST['number']
    g = request.POST['status']
    mem = Member.objects.get(id=id)
    mem.lastname = a
    mem.firstname = b
    mem.post = c
    mem.date = d
    mem.email = e
    mem.number = f
    mem.status = g
    mem.save()
    return redirect("/")