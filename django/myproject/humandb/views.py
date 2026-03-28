from django.shortcuts import render, redirect
from .models import Human


def index(request):
    humans = Human.objects.all()
    selected = None

    if request.method == 'POST':
        action = request.POST.get('action')
        first_name = request.POST.get('first_name')

        try:
            selected = Human.objects.get(first_name=first_name)
        except:
            selected = None

        if action == 'update' and selected:
            selected.last_name = request.POST.get('last_name')
            selected.phone = request.POST.get('phone')
            selected.address = request.POST.get('address')
            selected.city = request.POST.get('city')
            selected.save()

        elif action == 'delete' and selected:
            selected.delete()
            return redirect('/human/')

    return render(request, 'index.html', {
        'humans': humans,
        'selected': selected
    })