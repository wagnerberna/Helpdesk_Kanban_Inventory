from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


# Create your views here.
@login_required
def home(request):
    return render(request, "global/home.html", context={"title": "Home"})


def logout_user(request):
    logout(request)
    return redirect("home")


def access_denied(request):
    return render(request, "global/access_denied.html", context={"title": "Home"})
