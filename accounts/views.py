from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# from .forms import RegisterUserForm   # 상대 경로
from accounts.forms import RegisterUserForm  # 절대 경로


# Create your views here.

# class HTTPRequest :
#   POST = {"username" : "admin", "password" : "1234"}


# dev_9
def login_user(request):

    if request.method == "POST":
        # username = request.POST.get("username", "") 가 더 안전 / username이 없으면 빈 칸으로 대체
        username = request.POST["username"]  # username이 없으면 죽음
        password = request.POST["password"]

        # DB에 있는지를 조회하고 대조
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "로그인이 되었습니다.")
            return redirect("/")

        else:
            messages.success(
                request, "로그인이 실해했습니다. 다시 한 번 더 시도해주시기 바랍니다."
            )
            # return redirect("accounts:login_user")
            return redirect("accounts/login/")
    else:
        return render(request, "accounts/login.html", {})


# dev_9
def logout_user(request):
    logout(request)  # session에 저장된 sessionid 삭제
    return redirect("/")


# dev_10
def register_user(request):

    form = RegisterUserForm()

    if request.method == "POST":
        print(form)
    else:
        context = {"form": form}

    return render(request, "accounts/register.html", context)
