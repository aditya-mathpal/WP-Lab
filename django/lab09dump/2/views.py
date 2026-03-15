from django.shortcuts import render, redirect
from .models import Works, Lives
from .forms import WorksForm, CompanySearchForm


def index(request):
    return render(request, 'index.html')


def add_work(request):
    form = WorksForm()

    if request.method == 'POST':
        form = WorksForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/company/')

    return render(request, 'add_work.html', {'form': form})


def search_company(request):
    form = CompanySearchForm()
    results = None

    if request.method == 'POST':
        form = CompanySearchForm(request.POST)

        if form.is_valid():
            company = form.cleaned_data['company_name']

            works = Works.objects.filter(company_name=company)

            results = []
            for w in works:
                lives = Lives.objects.filter(person_name=w.person_name)

                for l in lives:
                    results.append({
                        'person': w.person_name,
                        'city': l.city
                    })

    return render(request, 'search_company.html', {
        'form': form,
        'results': results
    })