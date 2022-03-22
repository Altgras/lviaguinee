from django.shortcuts import render

# Create your views here.
def readers(request):
    context = {
        'tooltip': 'Lecteurs',

    }
    return render(request, 'reader/readers.html', context)


def add_reader(request):
    context = {
        'tooltip': "Ajout d'un lecteur",

    }
    return render(request, 'reader/add_reader.html', context)