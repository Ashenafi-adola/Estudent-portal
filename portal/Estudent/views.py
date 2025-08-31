from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Student_informations
from .forms import RegistForm
# Create your views here.
key = 0
def login(response):
    global key
    key = 0
    stud = Student_informations.objects.all()
    if response.method == 'POST':
        for  i in stud:
            if i.IdentityCard == response.POST.get("Username") and i.Password == response.POST.get("password"):
                key = i.id
                return HttpResponseRedirect(f"/home/")

    return render(response, "Estudent/login.html", {})
def registration(response):
    form = RegistForm()
    if Student_informations.objects.first() == None:
        n = 23434
    else:
        a = Student_informations.objects.last()
        n = a.No + 1
        
    if response.method == 'POST':
        form = RegistForm(response.POST, response.FILES)
        if response.POST.get('Password') == response.POST.get('Password_confirmation'):
            stud = Student_informations(
                Name = response.POST.get("First_name"),
                Father = response.POST.get("Father_name"),
                GrandFather = response.POST.get("Grandfather_name"),
                Gender = response.POST.get("Gender"),
                MaritalStatus = response.POST.get("Marital_status"),
                MatricResult = response.POST.get("Matriculation"),
                DateOfBirth = response.POST.get("Date Of Birth"),
                Age = response.POST.get("Age"),
                PlaceOfBirth = response.POST.get("Place_of_birth"),
                Photo = response.POST.get("Photo"),
                Nationality = response.POST.get("Nationality"),
                Region = response.POST.get("Region"),
                Disability = response.POST.get("Disability"),
                Email = response.POST.get("Email"),
                Phone = response.POST.get("Phone"),
                Password = response.POST.get("Password"),
                IdentityCard = f"ugr/{n}/18",
                No = n
            )
            stud.save()
    return render(response, "Estudent/registration.html",{"form":form})
def home(respose):
    a = Student_informations.objects.get(id=key)
    return render(respose, "Estudent/home.html",{"a":a,"id":id})
def studentProfile(response):
    a = Student_informations.objects.get(id=key)
    return render(response, "Estudent/studprof.html", {"a":a,"id":key})
def appilicant(responmse):
    a = Student_informations.objects.get(id = key)
    return render(responmse, "Estudent/applicant.html", {"a":a, "id":key})