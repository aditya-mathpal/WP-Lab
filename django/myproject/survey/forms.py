from django import forms

class SurveyForm(forms.Form):
    CHOICES = [
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('bad', 'Bad'),
    ]

    choice = forms.ChoiceField(
        label="How is the book ASP.NET with C# by Vipul Prakashan?",
        choices=CHOICES,
        widget=forms.RadioSelect,
        required=True
    )