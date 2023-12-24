from django.shortcuts import render, redirect, HttpResponse
from app import models


def init(request):
    return redirect("index/")


def index(request):
    return render(request, "index.html")


def close(request):
    return render(request, "shutdown.html")


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        account = request.POST.get("account")
        password = request.POST.get("password")

        data = models.Login.objects.filter(account=account, password=password).first()
        if data:
            return redirect("../success.html")
        else:
            return redirect("../login_error.html")


def login_error(request):
    return render(request, "login_error.html")


def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    else:
        account = request.POST.get("account")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if len(account) < 8 or len(account) > 18:
            # 用session传递参数
            request.session['error'] = "账号长度不符合要求"
            return redirect("register_error")
        elif len(password1) < 4 or len(password1) > 12:
            request.session['error'] = "密码长度不符合要求"
            return redirect("register_error")
        elif password1 == password2:
            try:
                models.Login.objects.create(account=account, password=password1)
                return redirect("../login.html")
            except Exception as e:
                request.session['error'] = e
                return redirect("register_error")
        else:
            request.session['error'] = "输入密码不一致"
            return redirect("register_error")


def register_error(request):
    error = request.session['error']
    return render(request, "register_error.html", {"error": error})


def success(request):
    return render(request, "success.html")
