from django.shortcuts import render

# Create your views here.

def dashboard(request):
    context = {
        'tooltip':'Tableau de bord',
    }
    return render(request,'book/dashboard.html',context)


def ranks(request):
    context = {
        'tooltip':'Gestion des Rayons',

    }
    return render(request,'book/ranks.html',context)

def read_points(request):
    context = {
        'tooltip':'Points de lectures',

    }
    return render(request,'book/readpoints.html',context)

def books(request):
    context = {
        'tooltip':'Livres',

    }
    return render(request,'book/books.html',context)


def edit(request,id):
    context = {
        'tooltip':'Livres',

    }
    return render(request,'book/books.html',context)
