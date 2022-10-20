from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone


def index(request):
    return render(request, "index.html", {"list" : MyBoard.objects.all()})
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # index.html를 리턴? MyBoard.objects.all()값을 list라는 키값에 담아서 리턴

def detail(request, id):
    return render(request, "detail.html", {"dto" : MyBoard.objects.get(id=id)})

def insert_form(request):
    return render(request, "insert.html")

def insert_res(request):
    myname = request.POST["myname"]
    mytitle = request.POST["mytitle"]
    mycontent = request.POST["mycontent"]
    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect("index") #원래는 /insertres/로 가야되는데 redirect해서 name이 index인 url로 가라는거임.
    else:
        return redirect("insertform") # 바뀐게 없으면 아까 게시판 글 작성 화면으로 돌아가라는 것.