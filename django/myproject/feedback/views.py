from django.shortcuts import render
from .forms import FeedbackForm


def feedback_page(request):
    message = None

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']

            if gender == "Male":
                prefix = "Mr"
            else:
                prefix = "Ms"

            message = f"Thanks {prefix} {name} for your feedback."
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {
        "form": form,
        "message": message
    })