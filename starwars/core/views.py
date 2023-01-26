from django.shortcuts import render, redirect, HttpResponse

from .models import Metadata

from .utils.operations import download_data


def people(request):
    return render(request, 'core/people.html')


def collections(request):
    files = Metadata.objects.all()
    context = {
        'files': files
    }
    return render(request, 'core/collections.html', context)


def download(request):
    filename, download_date, request = download_data()

    return render(request, 'core/collections.html')

