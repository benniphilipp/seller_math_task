from django.shortcuts import render
from django.db.models import Sum
import csv

from .forms import UploadForm
from .models import CsvSeller
from django.views import View
from seller_math.services import store_csv_data


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
        csv_list = CsvSeller.objects.all()
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = form.cleaned_data.get('csv_file')
            store_csv_data(csv_file)

        context = {
            'csv_list': csv_list,
            'form': form,
        }

        return render(request, self.template_name, context)


#View List
class DeatileView(View):
    template_name = "detail.html"

    def get(self, request, *args, **kwargs):

        sort_zip = CsvSeller.objects.values("zip").annotate(summe=Sum('summe')).order_by("zip")
        
        context = {
            'csv_data': sort_zip, 
        }

        return render(request, self.template_name, context)
