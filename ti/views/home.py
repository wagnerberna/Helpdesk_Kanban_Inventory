from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render
from ti.service.check_user_access import check_user_access


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print("login-user::", user)
            if user is not None:
                login(request, user)
                return redirect("home")
    form = AuthenticationForm()
    form.fields["username"].label = "Usuário"
    form.fields["password"].label = "Senha"

    return render(
        request=request,
        template_name="registration/login.html",
        context={"form": form},
    )


@login_required
def home(request):
    check_support_user = check_user_access(request)
    print("check_support_user:::", check_support_user)
    template_path = "global/home.html"
    context = {"support_check": check_support_user}

    return render(request, template_path, context)


def logout_user(request):
    logout(request)
    return redirect("home")


@login_required
def ChangePassword(request):
    if request.method == "POST":
        form_passoword = PasswordChangeForm(request.user, request.POST)
        if form_passoword.is_valid():
            user = form_passoword.save()
            update_session_auth_hash(request, user)
            return redirect("home")
    else:
        form_passoword = PasswordChangeForm(request.user)

    template_path = "ti/pages/change_password.html"
    context = {"form_passoword": form_passoword}
    return render(request, template_path, context)


def access_denied(request):
    template_path = "global/access_denied.html"
    return render(request, template_path)


def about(request):
    template_path = "global/about.html"
    return render(request, template_path)
