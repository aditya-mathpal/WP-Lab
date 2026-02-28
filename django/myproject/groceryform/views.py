from django.shortcuts import render

# Create your views here.

from .forms import GroceryForm

def grocery_view(request):
    prices = {
        'Wheat': 40,
        'Jaggery': 60,
        'Dal': 80,
    }

    selected_items = []
    
    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['items']
            
            for item in items:
                selected_items.append({
                    'name': item,
                    'price': prices[item]
                })
    else:
        form = GroceryForm()

    return render(request, "grocery.html", {
        'form': form,
        'selected_items': selected_items
    })