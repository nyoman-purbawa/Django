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
        ]
    }
    return render(request, 'blog/index.html', context)