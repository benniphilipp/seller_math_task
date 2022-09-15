from django.shortcuts import render, redirect
from django.db.models import Sum
import csv

from .forms import UploadForm
from .models import CsvSeller
from django.views import View
from seller_math.services import store_csv_data, get_list_data
from django.urls.base import reverse_lazy


# View Form
class indexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        form = UploadForm()
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = form.cleaned_data.get('csv_file')
            store_csv_data(csv_file)
            return redirect(reverse_lazy('detail'))
        
        context = {
            'form': form,
        }

        return render(request, self.template_name, context)


# View List
class DeatileView(View):
    template_name = "detail.html"

    def get(self, request, *args, **kwargs):

        sort_zip = get_list_data()
        
        context = {
            'csv_data': sort_zip,
        }

        return render(request, self.template_name, context)
