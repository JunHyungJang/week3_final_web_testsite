from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect,  Http404
from django.views.decorators.csrf import csrf_exempt
from testsite.on_game_data import ingameOPGG
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class on_game(APIView):
    def post(self, request):
        userId = request.data.get('userId')
        # renewalOPGG(userId)
        userOnGameData = ingameOPGG(userId)
        print(userOnGameData)
        idlist = []
        champlist = []

        if (len(userOnGameData['Names']) == 0):
            print("게임중이 아닙니다")
            return Response(status=404)
        else:
            idlist = userOnGameData['Names']
            champlist = userOnGameData['Champions']
            imgList = userOnGameData['Champion Images']
            print(idlist)
            print(champlist)
            return Response(status=200, data=[idlist, champlist, imgList])

def main(request):
    user_id = request.session.get('user')
    print("hello")
    if user_id:
        print("hello1")
        member = User.objects.get(pk = user_id)
        # member_data = {}
        # member_data['login'] = member
        print("hello3434")
        # print(member_data)
        return render(request, "users/main.html", {'member_data': member})
    # user_pk = request.session.get('user')

    # if user_pk:
    #     fuser =User.objects.get(pk = user_pk)
    #     return HTTPResponse(fuser.id)
    
    return render(request, "users/main.html", {'member_data': 'null'})

@csrf_exempt
def login_view(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        res_data = {}
        user  = authenticate(username = username, password = password)

        if user is not None:
            member = User.objects.get(username=username)
            print("인증성공")
            login(request,user)
            request.session['user'] = member.id
            return redirect("users:main")

        else:
            res_data['error'] = "비밀번호가 일치하지 않습니다."
            print("인증실패")
    return render(request,"users/login.html", res_data)
    

def logout_view(request):
    request.session.flush()
    logout(request)
    return redirect("users:main")

@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        print(111,request.POST)
        # profile_img = request.FILES["profile_img"]
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]

        user = User.objects.create_user(username,email,password)
        user.last_name = lastname
        user.first_name = firstname
        user.student_id = student_id
        # user.profile_img = profile_img
        user.save()

        return redirect("users:login")


    return render(request, "users/signup.html")

def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'users/list.html', boards)

def post(request):
    if not request.session.get('user'):
        return redirect("users:login")
    if request.method == "GET":
        board = Board()
    elif request.method == "POST":
        print("1222222222222222")
        user_id = request.session['user']
        author = User.objects.get(pk = user_id)
        print("1111111111111")
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author = author, title = title, content = content)
        board.save()

        return redirect("users:index")
    return render(request,'users/post.html')

def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'users/detail.html', {'board': board})

@csrf_exempt
def delete(request,id):
    if not request.session.get('user'):
        return redirect("users:login")
    board = Board.objects.get(pk = id)
    board.delete()
    return redirect("users:index")

def edit(request,id):
    if not request.session.get('user'):
        return redirect("users:login")
    board = Board.objects.get(pk = id)
    if request.method == "POST":
        board.title = request.POST["title"]
        board.author = request.POST["author"]
        board.content = request.POST["content"]

        board.save()

        return redirect("users:index")


    return render(request, 'users/edit.html', {'board' : board})