from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.objects.all()
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/student/')

    return render(request, 'index.html', {
        'form': form,
        'students': students
    })