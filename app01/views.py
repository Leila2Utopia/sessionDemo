from django.shortcuts import render,HttpResponse,redirect
from app01.models import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = UserInfo.objects.filter(username=username, pwd=pwd).first()
        if user:
            request.session["user_id"] = user.pk
            request.session["username"] = user.username

            '''
            cookie未过期且用户为非首次登陆，则更新django-sesion表中对应value值
            if request.COOKIE.get("sessionid"):
                更新
            
            用户为首次登陆时
            else:
                {"user_id": 1, "username": "lary"}
                第一步: 生成随机字符串: vwerascxh24asdasdasdsd
                第二步: 在django-sesion表生成一条记录:
                        session - key:vwerascxh24asdasdasdsd
                        session - data:{"user_id": 1, "username": "alex"}
                第三步:obj.set_cookie("sessionid", vwerascxh24asdasdasdsd)
            '''

            return HttpResponse('登录成功')
    return render(request, 'login.html')

def index(request):
    if not request.session.get("user_id"):
        return redirect('/login/')

    '''
    1 request.COOKIE.get("sessionid"):vwerascxh24asdasdasdsd
    2 在django-sesion表查询一条记录:session-key=vwerascxh24asdasdasdsd
    3 session-data({"user_id":1,"username":"alex"}).get("user_id")
    '''

    name = request.session.get("username")
    return render(request, "index.html", locals())