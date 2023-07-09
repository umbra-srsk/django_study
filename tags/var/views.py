from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'var/index.html')

def variable01(request):
    my_list = ['python', 'django', 'templates']
    return render(request, 'var/variable01.html', {'lst' : my_list})

def variable02(request):
    my_dict = {'class' : 'Data Engineer', 'name' : 'Kim SeokHo'}
    return render(request, 'var/variable02.html', {'dct' : my_dict})

def for_loop(request):
    return render(request, 'var/forloop.html', {'number' : range(1, 11)})

def if01(request):
    return render(request, 'var/if01.html', {'user' : {'id' : 'hong-gd'}})

def if02(request):
    member = {'id': 'multi', 'class': 'de', 'role': 'manager'}
    return render(request, 'var/if02.html',  member)

def href(request):
    return render(request, 'var/href.html')

def get_post(request):
    if request.method == 'GET':
        return render(request, 'var/get.html')
    elif request.method == 'POST':
        return render(request, 'var/post.html')
    else:
        return redirect('index')
