from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

# Create your views here.
def index(request):
    return render(request,"index/base.html")

class BlogListView(ListView):
    model = Course
    template_name = "index/index.html"

class CoursesView(ListView):
    model = Course
    template_name = "index/courses.html"

def about(request):
    return render(request,"index/about.html")