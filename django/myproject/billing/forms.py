from django import forms

class BillingForm(forms.Form):

    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('Nokia', 'Nokia'),
        ('Samsung', 'Samsung'),
        ('Motorola', 'Motorola'),
        ('Apple', 'Apple'),
    ]

    ITEM_CHOICES = [
        ('Mobile', 'Mobile'),
        ('Laptop', 'Laptop'),
    ]

    brand = forms.ChoiceField(
        choices=BRAND_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    items = forms.MultipleChoiceField(
        choices=ITEM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    quantity = forms.IntegerField(
        min_value=1,
        required=True
    )