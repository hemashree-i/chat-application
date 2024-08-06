from django.shortcuts import redirect, render
import channels
import daphne
from . models import *
from django.contrib import messages
# Create your views here.


def index(request):    
    if request.method == 'POST' and 'login' in request.POST:
        name=request.POST['username']
        password=request.POST['password']
        data=signin.objects.filter(username=name).all()
        rooms1=Room.objects.all()
        for i in data:
            print(i.username)
            if (i.username == name and i.password == password):
                return render(request, "chat/Rooms.html",{'rooms':rooms1 ,'name':name})
            else:
              return render(request, "chat/index.html")
    return render(request, "chat/index.html")


def sigin(request):
    if request.method=="POST" and 'signin' in request.POST:
        username=request.POST['username']
        password1=request.POST['Password']
        password2=request.POST['password1']
        # username1=signin.objects.filter(username=username).exists()
        # print("username")
        # print(username1)
        # if username1=='False':
        if password1==password2:
            signin.objects.create(
                username=username,
                password=password1
            )
            messages.info(request, "Signup process completed")
        else:
            messages.error(request, "Password not matched")
        # else:
        #     messages.error(request, "Username already exists")
    return render(request, "signin.html")

def room(request, room_name ,name ):
    message=chat_msg.objects.filter(room_chat=room_name).all()
    print(name)
    stored_msg=[]
    chat=[]
    chat1={}
    uname=[]
    for m in message:
        chat=m.chat
        uname=m.user_name
        chat1={
            "chat":chat,
            "uname":uname
        }
        stored_msg.append(chat1)
    return render(request, "chat/room.html", {"room_name": room_name ,"message": stored_msg,"name":name})
    
