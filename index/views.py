from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

# Create your views here.
def index(request):
    return render(request,"index/index.html")

class BlogListView(ListView):
    model = Course
    template_name = "index/index.html"