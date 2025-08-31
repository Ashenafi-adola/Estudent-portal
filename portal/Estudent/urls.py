from django.urls import path
from .import views
urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.registration , name="registration"),
    path("home/", views.home, name="home"),
    path("studProfile/", views.studentProfile, name="studProfile"),
    path("applicant/", views.appilicant, name="applicnat")
]
