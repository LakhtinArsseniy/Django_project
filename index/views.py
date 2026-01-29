from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {"article": {"date": "12.11.2024", "title": "Text here", "author": "<NAME>"}})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')