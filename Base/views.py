from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request,"master.html")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def skill(request):
    return render(request,"skills.html")
def resume(request):
    return render(request,"resume.html")
def project(request):
    return render(request,"projects.html")
def certificates(request):
    return render(request,"certificates.html")
def contact(request):
    return render(request,"contact.html")