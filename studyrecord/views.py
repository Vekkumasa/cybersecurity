from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Course
#filtered = Course.objects.raw("SELECT id, comments FROM studyrecord_Course where name='"+ coursename + "';")
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method=="POST" and "name" in request.POST:
        if request.POST.get("name") != "":
            if len(Course.objects.filter(user=request.user, name=request.POST.get("name"))) == 0:
                Course.objects.create(user=request.user, name=request.POST.get("name"), passed=False, grade=0)

    if request.method=="POST" and "coursename" in request.POST:
        coursename = request.POST.get("coursename")
        courses=Course.objects.filter(user=request.user)
        filtered = Course.objects.raw("SELECT id, comments FROM studyrecord_Course where name= %s;", [coursename])
        return render(request,"studyRecord/index.html",{"courses":courses, "filtered":filtered})

    courses=Course.objects.filter(user=request.user)
    return render(request,"studyRecord/index.html",{"courses":courses})

@login_required
@csrf_exempt
def singleCourseView(request, cid):
    course = Course.objects.get(id=cid)

    if request.method=="GET" and "modify" in request.GET:        
        if request.GET.get("passed"):
            course.passed = request.GET.get("passed")
            course.grade = request.GET.get("grade")
            course.comments = request.GET.get("comment")
        else:
            if request.GET.get("comment") != None:
                course.comments = request.GET.get("comment")
            course.passed = False       
            course.grade = 0
        course.save()

    if request.method=="GET" and "delete" in request.GET:
        Course.objects.get(id=cid).delete()
        courses=Course.objects.filter(user=request.user)
        return render(request, "studyRecord/index.html", {"courses":courses})
    return render(request,"studyRecord/course.html",{"course":course})

def loginpage(request):
    if request.GET.get("username") != None:
        user=authenticate(username=request.GET.get("username"), password=request.GET.get("password"))
        if user == None:
            return render(request,"studyRecord/login.html")
        else:
            login(request=request, user=user)
            return redirect("/")

    if request.user.is_authenticated:
        return redirect("/")

    return render(request,"studyRecord/login.html")
    
def createaccount(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method=="POST":
        User.objects.create_user(request.POST.get("username"),"", request.POST.get("password"))
        return redirect("login")
    return render(request,"studyRecord/createAccount.html")

def logoutpage(request):
    logout(request)
    return redirect("/")