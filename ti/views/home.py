from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from helpdesk.models import Support


@login_required
def check_user_access(request):
    id = request.user.pk
    check = Support.objects.filter(user_name=id)
    if not check:
        return False
    else:
        return True


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
            return redirect("index")
    else:
        form_passoword = PasswordChangeForm(request.user)

    template_path = "alterar_senha.html"
    context = {"form_passoword": form_passoword}
    return render(request, template_path, context)


def access_denied(request):
    template_path = "global/access_denied.html"
    return render(request, template_path)
