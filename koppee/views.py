from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from koppee.models import admindb,catdb,coffeedb,contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout







# Create your views here.


def indexpage(request):
    return render(request,"index.html")

def adminpage(request):
    return render(request,"addadmin.html")

def savedata(request):

    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        img = request.FILES['image']
        us = request.POST.get('uname')
        ps = request.POST.get('pswrd')
        cn = request.POST.get('cnfrm')
    obj = admindb(Name = na,Mobile = mob,Email = em,Image = img,Uname = us,Pswrd = ps,Cnfrm = cn)
    obj.save()
    return redirect(adminpage)

def display(request):
    data=admindb.objects.all()
    return render(request,"displayadmin.html",{'data':data})


def editpage(request, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(request, "editadmin.html", {'data':data})

def updatepage(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        us = request.POST.get('uname')
        ps = request.POST.get('pswrd')
        cn = request.POST.get('cnfrm')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=na,Mobile=mob,Email=em,Uname=us,Pswrd=ps,Cnfrm=cn,Image=file)
        return redirect(display)

def deletepage(request, dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(display)


def catpage(request):
    return render(request,"addcategory.html")

def datasave(request):
    if request.method == "POST":
        cn = request.POST.get('name')
        img = request.FILES['imag']
    obj = catdb(Catname=cn,Image=img)
    obj.save()
    return redirect(catpage)

def catdisplay(request):
    dt=catdb.objects.all()
    return render(request,"displaycategory.html",{'dt':dt})

def cateditpage(request, dataid):
    dt=catdb.objects.get(id=dataid)
    print(dt)
    return render(request, "editcat.html", {'dt':dt})

def catupdate(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('name')
        try:
            img = request.FILES['imag']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(Catname=cn,Image=file)
        return redirect(catdisplay)

def catdelete(request, dataid):
    dt=catdb.objects.filter(id=dataid)
    dt.delete()
    return redirect(catdisplay)


def coffeepage(request, dt=None):
    dat=catdb.objects.all()
    return render(request,"addcoffee.html",{'dat':dat,'dt':dt})


def coffeesave(request):
    if request.method == "POST":
        nam = request.POST.get('bname')

        pri = request.POST.get('price')
        ab = request.POST.get('abt')
        img = request.FILES['image']
        ca = request.POST.get('cat')
    obj = coffeedb(Coffeename=nam,Price=pri,About=ab,Image = img,Category=ca)
    obj.save()
    return redirect(coffeepage)

def coffeedisplay(request):
    dat=coffeedb.objects.all()
    return render(request,"displaycoffee.html",{'dat':dat})


def coffeeedit(request, dataid):
    dat=coffeedb.objects.get(id=dataid)
    da=catdb.objects.all()
    print(dat)
    return render(request, "editcoffee.html", {'dat':dat,'da':da})

def coffeeupdate(request, dataid):
    if request.method == "POST":
        nam = request.POST.get('bname')

        pri = request.POST.get('price')
        ab = request.POST.get('abt')
        ca = request.POST.get('cat')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = coffeedb.objects.get(id=dataid).Image
        coffeedb.objects.filter(id=dataid).update(Coffeename=nam,Price=pri,About=ab,Image = file,Category=ca)
        return redirect(coffeedisplay)

def coffeedelete(request, dataid):
    dat=coffeedb.objects.filter(id=dataid)
    dat.delete()
    return redirect(coffeedisplay)

def adminloginpage(request):
    return render(request,"adminlogin.html")

def adminlog(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(adminloginpage)
        else:

            return redirect(adminloginpage)
def contpage(request):
    data =contactdb.objects.all()
    return render(request,"contactdisplay.html",{'data':data})

def deletecontact(request, dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(contpage)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminloginpage())


