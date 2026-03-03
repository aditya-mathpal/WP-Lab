from django.shortcuts import render, redirect
from .forms import SurveyForm

# Create your views here.

good_votes = 0
satisfactory_votes = 0
bad_votes = 0

def survey(request):
    global good_votes, satisfactory_votes, bad_votes

    if request.method == "POST":
        form = SurveyForm(request.POST)

        if form.is_valid():
            choice = form.cleaned_data['choice']

            if choice == "good":
                good_votes += 1
            elif choice == "satisfactory":
                satisfactory_votes += 1
            elif choice == "bad":
                bad_votes += 1
            
            return redirect('result')
    else:
        form = SurveyForm()

    return render(request, "vote.html", {"form": form})

def result(request):
    total = good_votes + satisfactory_votes + bad_votes

    good_percent = (good_votes / total) * 100
    satisfactory_percent = (satisfactory_votes / total) * 100
    bad_percent = (bad_votes / total) * 100

    context = {
        "good": good_percent,
        "satisfactory": satisfactory_percent,
        "bad": bad_percent,
    }

    return render(request, "result.html", context)