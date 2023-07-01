import os
import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.settings import ALLOWED_HOSTS
from .serializers import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')


class RegisterAPI(APIView):

    def post(self, request):
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        pass1 = request.POST['pass1'].strip()
        pass2 = request.POST['pass2'].strip()

        # checks for errror input
        if len(username) > 12:
            messages.error(request,"Username must be under 10 charactor.")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request,"password not same.")
            return redirect('/')

        # creating User
        owner = User.objects.create_user(username, email, pass1)
        owner.save()
        user_detail = UserDetail.objects.create(user=owner, status=False)
        user_detail.save()
        messages.success(request,"Register successfully.")
        return redirect('/')


class LoginAPI(APIView):

    def post(self, request):
        login_name = request.POST['username']
        login_pwd = request.POST['pwd']
        user = authenticate(username=login_name, password=login_pwd)
        if user is not None:
            login(request, user)
            obj = UserDetail.objects.get(user=user)
            obj.status = True
            obj.save()
            messages.success(request, 'Login successfully')
            return redirect('/api/online-users')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')


class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        obj = UserDetail.objects.get(user=request.user)
        obj.status = False
        obj.save()
        logout(request)
        messages.success(request, "Successfully logged out.")
        return redirect('/')


@login_required(login_url='/')
def onlineUsers(request):
    objs = UserDetail.objects.all()
    serializer = UserDetailSerializer(objs, many=True)
    data = json.loads(json.dumps(serializer.data))
    return render(request, 'home.html', {'data': data})


class ChatStartAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        obj = UserDetail.objects.get(id=pk)
        serializer = UserDetailSerializer(obj)
        data = json.loads(json.dumps(serializer.data))
        room_code = f"{data['user']['id']}_{request.user.id}"
        messages = []
        try:
            room = ChatRoom.objects.get(room_code=room_code)
            chats = ChatMsg.objects.filter(room=room)
            chats_obj = ChatMessageSerializer(chats, many=True)
            messages = json.loads(json.dumps(chats_obj.data))
        except:
            room_code = f"{request.user.id}_{data['user']['id']}"
            try:
                room = ChatRoom.objects.get(room_code=room_code)
                chats = ChatMsg.objects.filter(room=room)
                chats_obj = ChatMessageSerializer(chats, many=True)
                messages = json.loads(json.dumps(chats_obj.data))
            except:
                room_obj = ChatRoom.objects.create(room_code=room_code)
                room_obj.save()
                room_obj.users.add(obj.user, request.user)

        return render(request, 'chat.html', {'data' : data, 'room_code' : room_code, 'messages' : messages})



def suggestFriend(request, user_id):
    file = os.path.join(os.getcwd(), 'users.json')
    with open(file, 'rb') as fp:
        json_data = json.loads(fp.read())
    
    data = json_data['users']
    input_user = None
    for ind, user in enumerate(data):
        if user['id'] == user_id:
            input_user = data.pop(ind)
            break
    
    input_interest_keys = input_user['interests'].keys()

    extract_data = []
    for user in data:
        for interest in input_interest_keys:
            if interest not in user['interests']:
                break
        else:
            extract_data.append(user)
    
    filter_data = []
    for user in extract_data:
        maxi = 0
        for key in input_interest_keys:
            maxi += user['interests'][key]
        
        user['score'] = maxi
        filter_data.append(user)

    result_data = sorted(filter_data, key=itemgetter('score'), reverse=True)

    return JsonResponse({"Suggested Friends" : result_data[:5]}, status=status.HTTP_200_OK)





