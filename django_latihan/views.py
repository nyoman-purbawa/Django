from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Home', 
        'desc' : 'Ini Merupakan Halaman Home Yng Sesuai',
        'banner' : 'images/gambar_banner.jpg'
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')

def daftar(request):
    return render(request, 'daftar.html')