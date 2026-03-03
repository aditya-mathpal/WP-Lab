from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data.get('email')
            contact = form.cleaned_data.get('contact')

            context = {
                'username': username,
                'email': email,
                'contact': contact
            }

            return render(request, "success.html", context)
    else:
        form = RegisterForm()

    return render(request, "register.html", {'form': form})