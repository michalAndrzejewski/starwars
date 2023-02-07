from django.shortcuts import render, redirect

from .models import Metadata

from .utils.operations import download_data_from_api, convert_from_csv, get_value_count

ROWS_VALUE = 3

def homepage(request):
    return render(request, 'core/home.html')


def collections(request):
    files = Metadata.objects.all().order_by('-id')
    context = {
        'files': files
    }
    return render(request, 'core/collections.html', context)


def download_data(request):
    filename, download_date = download_data_from_api()
    Metadata.objects.create(
        filename=filename,
        download_date=download_date
    )
    return redirect('collections')


def single_collection(request, pk):
    collection = Metadata.objects.get(id=pk)
    people_data = convert_from_csv(collection.filename)
    value_count = get_value_count(collection.filename)
    context = {
        'collection': collection,
        'people': people_data,
        'value_count': value_count,
    }
    return render(request, 'core/single_collection.html', context)

