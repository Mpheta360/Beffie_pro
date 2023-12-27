from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from core.models import TrendProducts
from core.models import Gallery
from core.models import BlockProducts
from core.models import SlabProducts
from core.models import PaverProducts
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login,logout 
# Create your views here.

def home(request):
    return render(request, 'main.html')

def service(request):
    return render(request, 'services.html')

def choose(request):
    return render(request, 'choose.html')

def product(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    pictures=Gallery.objects.all()
    context = {"Gallery": pictures}
    return render(request, 'gallery.html', context)

def lovedproducts(request):
    products=TrendProducts.objects.all()
    data= {"TrendProducts": products}
    return render(request, 'lovedproducts.html', data)

def block(request):
    bproducts=BlockProducts.objects.all()
    bdata= {"BlockProducts": bproducts}
    return render(request, 'block.html', bdata)

def paver(request):
    pproducts=PaverProducts.objects.all()
    pdata= {"PaverProducts": pproducts}
    return render(request, 'paver.html', pdata)

def slab(request):
    sproducts=SlabProducts.objects.all()
    sdata= {"SlabProducts": sproducts}
    return render(request, 'slab.html', sdata)

def contact(request):
    return render(request, 'contact.html')

def lowani(request):
    if request.method =="POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        address = request.POST.get("address")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        myuser = User.objects.create_user(username, address, password)
        myuser.first_name= fname
        myuser.last_lame= lname

        myuser.save()

        messages.success(request, "Account created successfully. We have sent you email please activate your account.")
        return redirect('/login')
    return render( request,'lowani.html' )



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username= username, password= password)
        if user is not None:
            dj_login(request, user)
            messages.success(request, "Successfully logged in.")
            return render(request, "dashboard.html")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def out(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('/login')


def dashboard(request):
    return render(request, 'dashboard.html')

def details(request, id):
    prod= AllProducts.objects.get(id=id)
    context = {"title": prod.pname,
                "description": prod.pdescription,
                "price": prod.pprice,
                "image": prod.p_image
                }
    return render(request, 'productdetails.html', context)

