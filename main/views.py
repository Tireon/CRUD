from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout

from .models import Member, LoginUserForm


# Отображение всех записей
def index (request):
    mem = Member.objects.all()
    return render(request, 'main/index.html', {"mem":mem});

# Переход на страницу добавления новой записи
def  add(request):
    return render(request, 'main/add.html')

# Регистрация новой записи
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

# Удаление записи
def delete(PermissionRequiredMixin, id):
    permission_required = 'main.delete_member'
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

# Переход на страницу изменения существующей записи
def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'main/update.html',{'mem':mem})

# Изменение существующей записи
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

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'],
                                 password = cd['password'])
            if user:
                login(request, user)
                return redirect("/")
    else:
        form = LoginUserForm()
    return render(request, 'main/login_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect("/")