from django.shortcuts import render, redirect
from .models import Student_data
from .forms import StudentForm
from django.db.models import Q

def std_list(request):
    #students = Student_data.objects.all()
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    students = Student_data.objects.filter(
        Q(firstName__icontains=search_query) | 
        Q(lastName__icontains=search_query) |
        Q(mobileNumber__icontains=search_query)
    )


    context = {
        'students': students,
        'search_query': search_query,
    }
    return render(request, '/Users/juhigoel/Studentdetails/student/templates/list.html', context)
    

def create_student(request):
    form= StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students-list')

    context = {
        'form': form,
    }
    return render(request, '/Users/juhigoel/Studentdetails/student/templates/create.html', context)


def edit_student(request, pk):
    student = Student_data.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students-list')

    context = {
        'student': student,
        'form': form,
    }
    return render(request, '/Users/juhigoel/Studentdetails/student/templates/edit.html', context)


def delete_student(request, pk):
    student = Student_data.objects.get(id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students-list')

    context = {
        'student': student,
    }
    return render(request, '/Users/juhigoel/Studentdetails/student/templates/delete.html', context)
