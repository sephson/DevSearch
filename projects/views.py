from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


projectsList = [
        {
            'id': '1',
            'title': 'The Functioncal Web',
            'description': 'Fully working and works well'
        },
        {
            'id': '2',
            'title': 'The Social Media Project',
            'description': 'Chat with your friends from other continents'
        },
        {
            'id': '3',
            'title': 'Ecommerce Project',
            'description': 'Shop from the comfort of your home'
        }

    ]

def projects(request):
    page = 'page'
    number = 16
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
