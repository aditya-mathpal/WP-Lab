from django.shortcuts import render, redirect

# Create your views here.

from .forms import StudentForm


def first_page(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # Store data in session
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']

            return redirect('second')
    else:
        form = StudentForm()

    return render(request, "firstPage.html", {'form': form})


def second_page(request):
    name = request.session.get('name')
    roll = request.session.get('roll')
    subject = request.session.get('subject')

    context = {
        'name': name,
        'roll': roll,
        'subject': subject
    }

    return render(request, "secondPage.html", context)