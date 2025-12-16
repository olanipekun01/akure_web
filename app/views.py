from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, "index.html")

def About(request):
    return render(request, "about.html")

def AcademicCalendar(request):
    return render(request, "academic-calendar.html")

def DegreeProgrammes(request):
    return render(request, "degree-programmes.html")

def Tuition(request):
    return render(request, "tution.html")

def Admission(request):
    return render(request, "admissions.html")

def GeneralNursing(request):
    return render(request, "generalnursingdetails.html")