from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import data
from .form import ProductForm
con = data.objects.filter(published=True)
def home(req):
    return render(req,"home.html",{"con":con})
def show(req,post):
    dat = con.get(id=post)
    return render(req,"viewer.html",{"dat":dat})
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def new (req):
    if req.method=="POST":
        form = ProductForm(req.POST)  
        if form.is_valid():
            form.save()  
            return redirect("/") 
    else:
        form = ProductForm()    
    return render (req,"new.html")
@user_passes_test(lambda u: u.is_superuser)
def delete(req,bi):
    mod = data.objects.get(id=bi)
    mod.delete()
    render("/")
