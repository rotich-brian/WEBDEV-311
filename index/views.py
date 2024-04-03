from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Course

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    return render(request,"index/base.html")

class CoursesView(ListView):
    model = Course
    template_name = "index/courses.html"

def about(request):
    return render(request,"index/about.html")

def contact(request):
    return render(request,"index/contact.html")

@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class Dash_contact(ListView):
    model = Course
    template_name = "index/dashboard.html"

@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class CourseDetailView(DetailView):
    model = Course
    template_name = "index/course_detail.html"

@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class CourseDetailView_progress(DetailView):
    model = Course
    template_name = "index/detail-progress.html"

@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class CourseDetailView_materials(DetailView):
    model = Course
    template_name = "index/detail-materials.html"

@method_decorator(login_required(login_url='sign-in'), name='dispatch')
class CourseDetailView_community(DetailView):
    model = Course
    template_name = "index/detail-community.html"

def signin(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method =='POST':
            username1 = request.POST.get('username')
            password1 = request.POST.get('password')

            user = authenticate(request,username=username1, password=password1)

            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request,"Username and password does not match!")
                return render(request,"accounts/login.html")

        context={}
        return render(request,"accounts/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect('sign-in')

def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request,"Account Created successfully")
                return redirect('sign-in')


        context={'form':form}
        return render(request,"accounts/register.html",context)