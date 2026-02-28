from django import forms

class GroceryForm(forms.Form):
    ITEM_CHOICES = [
        ('Wheat', 'Wheat'),
        ('Jaggery', 'Jaggery'),
        ('Dal', 'Dal'),
    ]

    items = forms.MultipleChoiceField(
        choices=ITEM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Select Item:"
    )