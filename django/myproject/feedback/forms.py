from django import forms

class FeedbackForm(forms.Form):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    COURSE_CHOICES = [
        ('ASP-XML', 'ASP-XML'),
        ('DotNET', 'DotNET'),
        ('JavaPro', 'JavaPro'),
        ('Unix,C,C++', 'Unix,C,C++'),
    ]

    COVERAGE_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor'),
    ]

    name = forms.CharField(max_length=100, required=True)

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    course = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.Select,
        required=True
    )

    coverage = forms.ChoiceField(
        choices=COVERAGE_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    suggestion = forms.CharField(
        widget=forms.Textarea,
        required=False
    )