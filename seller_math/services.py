import csv
# from seller_math.views import decode_utf8
from seller_math.models import CsvSeller
import chardet
from django.db.models.aggregates import Sum


def decode_utf8(line_iterator):
    for line in line_iterator:
        yield line.decode('utf-8')


def store_csv_data(csv_file):
    csv_file.seek(0)
    data = csv_file.read()
    encoding = chardet.detect(data)
    encoded = encoding.get('encoding', "Windows-1254")
    lines = data.decode(encoded).splitlines()
    csv_data = csv.reader(lines, delimiter=';', quotechar='"')

    next(csv_data)  # Skip header row

    for counter, line in enumerate(csv_data):
        shipping_address_zip = line[17]
        total_price_with_shipping = line[6]
        c = CsvSeller()

        c.zip = shipping_address_zip
        c.summe = total_price_with_shipping
        c.save()


def get_list_data(**kw):
    sort_zip = CsvSeller.objects.values(
        "zip").annotate(summe=Sum('summe')).order_by("zip")
    return sort_zip

