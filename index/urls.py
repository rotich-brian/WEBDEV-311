from django.urls import path
from . import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/",views.CoursesView.as_view(), name="courses"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),

    path("course/<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),

    path("sign-up/",views.register,name="sign-up"),
    path("sign-in/",views.signin,name="sign-in"),
    path("sign-out/",views.logoutUser,name="sign-out"),

    path("dashboard/",views.Dash_contact.as_view(),name="dashboard"),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img-fav/favicon.ico'))),
]
