from django import forms

class CGPAForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        required=True
    )

    total_marks = forms.FloatField(
        label="Total Marks",
        required=True
    )