from ti.models import RestrictedArea


def check_user_access(request):
    id = request.user.pk
    check = RestrictedArea.objects.filter(user=id)
    if not check:
        return False
    else:
        return True
