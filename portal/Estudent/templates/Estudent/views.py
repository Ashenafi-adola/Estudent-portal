from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, OtherStudentDetails
# Create your views here.
def register(response):
    print(response.POST)
    if response.POST.get("Submit"):
        firstname = response.POST.get('Fname')
        fathername = response.POST.get('Sname')
        grandfathername = response.POST.get('Gname')
        gender = response.POST.get('gender')
        marital_status = response.POST.get('marital')
        matriculation = response.POST.get('matriculation')
        date_of_birth = response.POST.get('dob')
        age = response.POST.get('age')
        place_of_birth = response.POST.get('pob')
        photo = response.FILES.get('photo')
        nationality = response.POST.get('nationality')
        region = response.POST.get('region')
        disability = response.POST.get('disability')
        email = response.POST.get('email')
        phone = response.POST.get('phone')
        create_password = response.POST.get('password')
        confirm_password = response.POST.get('confirm_password')
        identity_card = f"ugr/{34}/18"
        if len(firstname) > 3 and len(fathername) > 3 and len(grandfathername) > 3 and len(matriculation) > 0 and len(email) > 5 and len(phone) == 10 :       
            student = Student(
                First_name=firstname,
                Father_name=fathername,
                Grandfather_name=grandfathername,
                Gender = gender,
                Marital_status = marital_status,
                Matriculation = matriculation,
                Date_of_birth = date_of_birth,
                Age = age,
                Place_of_birth = place_of_birth,
                Photo = photo,
                Nationality = nationality,
                Region = region,
                Disability = disability,
                Email = email,
                Phone = phone,
            )
            student.save() 
            other_details = OtherStudentDetails(
                Identity_card=identity_card,
                No=34,
                Password=create_password,
                Confirm_password=confirm_password
            )
            other_details.save()
            return HttpResponse("Registration successful") 
    return render(response, 'Estudent/registration.html',{})

def home(response):
    return render(response, 'Estudent/home.html',{})

def login(response):
    stud = Student.objects.all()
    
    return render(response, 'Estudent/login.html', {})
def studprofile(response):
    stu = Student.objects.get(id=1) # Assuming you want to get the first student  # Adjust this as needed to get the correct student
    return render(response, 'Estudent/studprof.html', {"stu": stu})