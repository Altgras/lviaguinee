from django.shortcuts import render

# Create your views here.
def subscriptions(request):
    context = {
        'tooltip': 'Abonnements ',
    }
    return render(request, 'subscription/subscriptions.html', context)


def resubscriptions(request):
    context = {
        'tooltip': 'Réabonnements ',
    }
    return render(request, 'subscription/resubscriptions.html', context)