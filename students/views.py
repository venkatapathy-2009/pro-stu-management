from django.shortcuts import render,redirect
from .models import student
from .forms import stu_form
def home(request):
    stu_obj=student.objects.all()
    return render(request,'home.html',{'stu_obj':stu_obj})
def ad(request):
    forms=stu_form()
    if request.method == "POST":

        forms=stu_form(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect ('home')
        else:
            forms=stu_form()
    return render(request,'add.html',{'forms':forms})