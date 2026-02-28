from django import forms

class StudentForm(forms.Form):
    SUBJECT_CHOICES = [
        ('Maths', 'Maths'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Computer Science', 'Computer Science'),
    ]

    name = forms.CharField(max_length=100, label="Name")
    roll = forms.CharField(max_length=20, label="Roll")
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, label="Subject")