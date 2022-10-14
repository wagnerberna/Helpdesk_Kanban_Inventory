from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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


def access_denied(request):
    template_path = "global/access_denied.html"
    return render(request, template_path)
