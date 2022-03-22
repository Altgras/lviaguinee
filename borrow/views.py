from django.shortcuts import render

# Create your views here.
def borrows(request):
    context = {
        'tooltip':'Gestion des Emprunts',

    }
    return render(request,'borrow/borrows.html',context)

def add_borrow(request):
    context = {
        'tooltip':"Ajout d'un emprunt",

    }
    return render(request,'borrow/addborrow.html',context)

def returns(request):
    context = {
        'tooltip':"Enregistrement d'un retour",
    }
    return render(request,'borrow/returns.html',context)