from django.shortcuts import render, redirect
from .forms import BillingForm

PRICE_LIST = {
    'HP': {'Mobile': 20000, 'Laptop': 50000},
    'Nokia': {'Mobile': 15000, 'Laptop': 40000},
    'Samsung': {'Mobile': 25000, 'Laptop': 55000},
    'Motorola': {'Mobile': 18000, 'Laptop': 42000},
    'Apple': {'Mobile': 60000, 'Laptop': 100000},
}


def billing_page(request):
    if request.method == "POST":
        form = BillingForm(request.POST)

        if form.is_valid():
            brand = form.cleaned_data['brand']
            items = form.cleaned_data['items']
            quantity = form.cleaned_data['quantity']

            total = 0
            for item in items:
                total += PRICE_LIST[brand][item] * quantity

            request.session['brand'] = brand
            request.session['items'] = items
            request.session['quantity'] = quantity
            request.session['total'] = total

            return redirect('bill_result')
    else:
        form = BillingForm()

    return render(request, "billing.html", {"form": form})


def bill_result(request):
    context = {
        "brand": request.session.get('brand'),
        "items": request.session.get('items'),
        "quantity": request.session.get('quantity'),
        "total": request.session.get('total'),
    }

    return render(request, "bill_result.html", context)