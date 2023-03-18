from django.shortcuts import render,redirect
from.models import studentData
def homePage(request):
    students=studentData.objects.all()
    return render(request,'homepage.html',{'students':students})
def add_student(request):
    if request.method == "GET":
        return render(request,'add_student.html')
    else:
        studentData(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        course=request.POST.get('course'),
        fee=request.POST.get('fee'),
        assignment1=request.POST.get('a1'),
        assignment2=request.POST.get('a2'),
        assignment3=request.POST.get('a3'),
        assignment4=request.POST.get('a4'),
        institute=request.POST.get('institute'),
        location=request.POST.get('location')
        ).save()
        return redirect('homepage')

def update_student(request, id):
    student=studentData.objects.get(id=id)
    if request.method == "GET":
        return render(request,'update_student.html',{'student':student})
    else:
        student.first_name=request.POST.get("fname")
        student.last_name=request.POST.get("lname")
        student.course=request.POST.get("course")
        student.fee=request.POST.get("fee")
        student.assignment1=request.POST.get("a1")
        student.assignment2=request.POST.get("a2")
        student.assignment3=request.POST.get("a3")
        student.assignment4=request.POST.get("a4")
        student.institute=request.POST.get("institute")
        student.location=request.POST.get("location")
        student.save()
        return redirect('homepage')

def delete_student(request, id):
    student=studentData.objects.get(id=id)
    student.delete()
    return redirect('homepage')





# Create your views here.
