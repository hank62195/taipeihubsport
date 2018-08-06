from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User #New Added

from hello import models
from hello import Team
#from ppb.models import member #New Added
#from ppb.models import team #New Added

# Create your views here.
def index(request): #New Added 0731
    '''mem = member.objects.all().order_by('mid')
    
    if request.user.is_authenticated:
        name = request.user.first_name
        ID = request.user.username
        balance = ''
        for i in mem:
            if i.mid == ID:
                balance = i.mMoney'''
    return render(request, 'index.html')

def db(request): #顯示資料表
    mem = member.objects.all().order_by('mid') #New Added
    return render(request, 'db.html', locals()) #New Added

def team(request): #顯示資料表
    team = Team()
    team.save()
    team = Team.objects.all().order_by('tId') #New Added
    return render(request, 'team.html', {'teams': teams}) #New Added

def game(request): #下注列表
    return render(request, 'game.html', locals()) #New Added

def register(request): #註冊
    postform = RegisterForm(request.POST) #此行沒有則一開始網頁無表格
    if request.method =='POST':
        postform = RegisterForm(request.POST)
        if postform.is_valid():
            
            mid = postform.cleaned_data['mid']
            mName = postform.cleaned_data['mName']
            mDepartment = postform.cleaned_data['mDepartment']
            mEmail = postform.cleaned_data['mEmail']
            mPassword = postform.cleaned_data['mPassword']

            try:
                m = member.objects.get(mid=mid)
            except:
                m = None

            if m!= None:
                message = '員編 ' + m.mid + '已註冊過!'
            else:
                unit = member.objects.create(mid =mid, mName = mName, mDepartment= mDepartment,
                                     mEmail = mEmail, mPassword= mPassword)
                unit.save()
                user = User.objects.create_user(mid,mEmail,mPassword) #同時寫入django內建使用者名單
                user.first_name = mName
                user.is_staff = False
                user.save()
                return redirect('/login')
        else:
            message = 'Email資料格式錯誤'

    return render(request, "register.html", locals())
    '''
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form}) #提供register 的變數給register.html讀取
    '''
'''
def register(request):
    postform = 
    return render(request, "register.html", locals())
'''
    
def manager(request): #報名成功訊息頁面
    return render(request, 'manager.html')

def login(request): #登入
    if request.method =="POST":
        ID = request.POST['username']
        pw =request.POST['password']
        user = auth.authenticate(username=ID, password=pw)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/index')
                message = '登入成功'
            else:
                message = '帳號未啟用' #?????
        else:
            message = '登入失敗' #????
    return render(request, 'login.html', locals())
'''
    try:
        del request.session['username']
    except:
        pass
    username='1234' #真正的帳密
    password='123'
    status=''
    if request.method =="POST":
        if not 'username' in request.session:
            if request.POST['username'] ==username and request.POST['password'] ==password:
                request.session['username'] = username
                message = username + '您好, 登入成功!' ####
                status = 'login'
    else:
        if 'username' in request.session:
            if request.session['username'] == username:
                message = request.session['username'] + '您已登入過了'
                status = 'login'
'''
    

def logout(request): #也可以回到首頁
    auth.logout(request)
    return redirect('/index')

