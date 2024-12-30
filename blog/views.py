from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title' : 'Blog',
        'desc' : 'Ini adalah halaman Blog yang real',
        'nav' : [
            ['/', 'Home'],
            ['', 'Blog'],
            ['article/', 'Article'],
            ['berita/', 'Berita'],
        ],
        'banner':  'blog/images/gambar_banner.jpg'
    }
    return render(request, 'blog/index.html', context)

def detail(request):
    return render(request, 'blog/detail.html')