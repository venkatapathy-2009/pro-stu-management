from django.shortcuts import render,redirect,get_object_or_404
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
def remove(request,pk):
    rem=student.objects.get(id=pk)
    rem.delete()
    return redirect('home')
def edit(request,pk):
    edit = get_object_or_404(student,pk=pk)
    forms=stu_form(instance=edit)
    if request.method == "POST":
        forms=stu_form(request.POST,instance=edit)
        if forms.is_valid():
            forms.save()
            return redirect ('home')
        else:
            forms=stu_form(instance=edit)
    return render(request,'edit.html',{'forms':forms})
    