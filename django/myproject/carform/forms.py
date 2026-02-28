from django import forms

class CarForm(forms.Form):
    CAR_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Hyundai', 'Hyundai'),
    ]

    manufacturer = forms.ChoiceField(
        choices=CAR_CHOICES,
        label="Select Car Manufacturer"
    )

    model_name = forms.CharField(
        max_length=100,
        label="Enter Model Name"
    )