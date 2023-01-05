from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as user_login
from  django.contrib.auth import logout as user_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Destination,Bus,BookBus

# Create your views here.

def home(request):
    current_user = request.user
    context={
        'current_user':current_user
    }
    return render(request,"home/index.html", context)

def about(request):
    current_user = request.user
    context={
        'current_user':current_user
    }
    return render(request,"about/about.html", context)

def login(request):
    current_user = request.user
    context={
        'current_user':current_user
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            user_login(request,user)
            messages.success(request, "Log in Successful")
            return redirect("home")
        else:
            messages.warning(request, "User not found...")
    return render(request,"auth/login.html", context)

def register(request):
    current_user = request.user
    context={
        'current_user':current_user
    }
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        ConfirmPassword = request.POST.get("ConfirmPassword")
        
        if password != ConfirmPassword:
            messages.warning(request, "Passwords do not match" )
            
        elif password == ConfirmPassword:
            User.objects.create_user(username,email,password)
            messages.success(request,"Account created successfully")
           
            return redirect("login")
    return render(request,"auth/register.html", context)

@login_required(login_url="login")
def logout(request):
    user_logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")

@login_required(login_url="login")
def destination(request):
    current_user = request.user
    bus = Bus.objects.all()
    destinations = Destination.objects.all()
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        car = request.POST.get("car")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        destination = request.POST.get("destination")
        book = BookBus.objects.filter(user= current_user.id).first()
        if book is None:            
            book_new_ticket = BookBus.objects.create(
                user = current_user,
                bus = car,
                first_name=first_name,
                last_name =last_name,
                email =email,
                contact =contact,
                destination = destination
            )
            
            book_new_ticket.save()
            bus = Bus.objects.filter(bus_name=car).first()
            if bus:
                print(bus)
                
            messages.success(request, "Ticket Booked Successfully")
            return redirect('home')
        else:
            messages.warning(request,"You have already booked a ticket")
            return redirect('destination')

    context={
        'current_user':current_user,
        'destinations':destinations,
        'bus':bus
    }
    return render(request,"destination/destination.html", context)

@login_required(login_url="login")
def profile(request):
    current_user = request.user
    booking_history = BookBus.objects.filter(user = current_user)   
    context={
        "current_user":current_user,
        "booking_history":booking_history
        
    }
    return render(request,"auth/profile.html",context)

def booking_history(request):
    current_user = request.user
    booking_history = BookBus.objects.filter(user = current_user) 
    context={
        "current_user":current_user,
        "booking_history":booking_history
    }
    return render(request,"destination/booking_history.html",context)