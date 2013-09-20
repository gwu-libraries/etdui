from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {
        'title': 'home',
    })

def results(request):
    return render(request, 'results.html', {
	'title': 'results',
    })

def item(request):
    return render(request, 'item.html', {
	'title': 'item details',
    })
