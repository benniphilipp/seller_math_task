from django import forms
from .models import CsvSeller


class UploadForm(forms.Form):
    csv_file = forms.FileField(
        required=False, widget=forms.FileInput(
            attrs={'class': 'form-control', 'placeholder':
            'Upload "products.csv"', 'help_text': 'Choose a .csv file with products to enter'}
            )
        )