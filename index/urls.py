from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/",views.CoursesView.as_view(), name="courses"),
    path("about/",views.about, name="about"),
]
