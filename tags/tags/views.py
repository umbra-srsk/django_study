from django.shortcuts import render

def index(request):
    return render(request, 'tags/index.html', {'name' : '김석호'})