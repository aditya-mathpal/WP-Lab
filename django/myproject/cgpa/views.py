from django.shortcuts import render, redirect
from .forms import CGPAForm

def page1(request):
    if request.method == "POST":
        form = CGPAForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            total_marks = form.cleaned_data['total_marks']

            cgpa = total_marks / 50

            request.session['name'] = name
            request.session['cgpa'] = cgpa

            return redirect('page2')
    else:
        form = CGPAForm()

    return render(request, "page1.html", {"form": form})


def page2(request):
    name = request.session.get('name')
    cgpa = request.session.get('cgpa')

    context = {
        "name": name,
        "cgpa": cgpa
    }

    return render(request, "page2.html", context)