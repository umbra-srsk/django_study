from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone

def index(request):
    myboard_all = MyBoard.objects.all().order_by('-id')
    print(myboard_all)
    return render(request, 'index.html', {'list': MyBoard.objects.all().order_by('-id')})

def insert_proc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    else:
        myname = request.POST['myname']
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']

        result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
        print(result)

        if result:
            return redirect('index')
        else:
            return redirect('insert')

"""
def insert_form(request):
    return render(request, 'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']


    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
    print(result)

    if result:
        return redirect('index')
    else:
        return redirect('insert')
"""

def detail(request, id):
    myboard_one = MyBoard.objects.get(id=id)
    print(myboard_one)
    return render(request, 'detail.html', {'dto': myboard_one})

def update_proc(request, id):
    if request.method == 'GET':
        myboard_one = MyBoard.objects.get(id=id)
        print(myboard_one)
        return render(request, 'update.html', {'dto': myboard_one})
    else:
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']
        #id = request.POST['id']

        myboard = MyBoard.objects.filter(id=id)
        print(myboard)
        result_title = myboard.update(mytitle=mytitle)
        result_content = myboard.update(mycontent=mycontent)
        print(f'title update : {result_title} / content update : {result_content}')

        if result_title + result_content == 2:
            return redirect(f'/detail/{id}')
        else:
            return redirect(f'/update/{id}')


"""
def update_form(request, id):
    myboard_one = MyBoard.objects.get(id=id)
    print(myboard_one)
    return render(request, 'update.html', {'dto': myboard_one})

def update_res(request):
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    id = request.POST['id']

    myboard = MyBoard.objects.filter(id=id)
    print(myboard)
    result_title = myboard.update(mytitle=mytitle)
    result_content= myboard.update(mycontent=mycontent)
    print(f'title update : {result_title} / content update : {result_content}')

    if result_title + result_content == 2:
        return redirect(f'/detail/{id}')
    else :
        return redirect(f'/updateform/{id}')
"""

def delete_proc(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()
    #print(result_delete)
    '''
        myboard = MyBoard.objects.get(id=id)
        myboard.mytitle = mytitle
        myboard.mycontent = mycontent
        myboard.save()
    '''

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect(f'/detail/{id}')

    '''
        myboard = MyBoard(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
        myboard.save()
    '''


