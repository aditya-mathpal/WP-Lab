from django.shortcuts import render

# Create your views here.

from .forms import RegForm, GeeksForm

def home_view(request):
    context = {}
    form = RegForm(request.POST or None)
    context['form'] = form
    return render(request, "home.html", context)