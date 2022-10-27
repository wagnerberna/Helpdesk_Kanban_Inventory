from django.contrib.auth.decorators import login_required
from helpdesk.models import Support


@login_required
def check_user_access(request):
    id = request.user.pk
    check = Support.objects.filter(user_name=id)
    if not check:
        return False
    else:
        return True
