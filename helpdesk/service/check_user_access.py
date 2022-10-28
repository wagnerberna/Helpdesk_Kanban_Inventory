from django.contrib.auth.decorators import login_required
from helpdesk.models import Support

#  <QuerySet [<Support: wagner.berna>]>
# print("check:::", check.values("user_name")[0])

# Retorna erro 404
# @login_required
# def check_user_permission(request):
#     id = request.user.pk
#     check = get_object_or_404(Support, user_name=id)
#     return check


@login_required
def check_user_access(request):
    id = request.user.pk
    check = Support.objects.filter(user_name=id)
    if not check:
        return False
    else:
        return True
