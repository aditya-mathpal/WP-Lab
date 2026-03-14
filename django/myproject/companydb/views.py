from django.shortcuts import render, redirect
from .forms import WorksForm, CompanyForm
from .models import Works, Lives


def insert_works(request):
    form = WorksForm()

    if request.method == 'POST':
        form = WorksForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/company/insert/')

    return render(request, 'insert_works.html', {'form': form})


def search_company(request):
    results = []

    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            company = form.cleaned_data['company_name']

            works_people = Works.objects.filter(company_name=company)

            for w in works_people:
                try:
                    l = Lives.objects.get(person_name=w.person_name)

                    results.append({
                        'name': w.person_name,
                        'city': l.city
                    })

                except Lives.DoesNotExist:
                    pass
    else:
        form = CompanyForm()

    return render(request, 'search_company.html', {
        'form': form,
        'results': results
    })