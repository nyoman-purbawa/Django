from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Home', 
        'desc' : 'Ini Merupakan Halaman Home Yng Sesuai'
    }
    return render(request, 'index.html', context)