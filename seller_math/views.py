from django.shortcuts import render
from django.db.models import Sum
import csv

from .forms import UploadForm
from .models import CsvSeller
from django.views import View




def decode_utf8(line_iterator):
    for line in line_iterator:
        yield line.decode('utf-8')

#View 
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
            csv_file = form.cleaned_data['csv_file']
            csv_data = csv.reader(decode_utf8(request.FILES['sent_file']))
            next(csv_data)  # Skip header row


        for counter, line in enumerate(csv_data):
            shipping_address_zip = line[18]
            total_price_with_shipping = line[7]

            c = seller_summ
            c.zip = shipping_address_zip
            c.summe = total_price_with_shipping
            c.save()



        context = {
            'csv_list': csv_list,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)