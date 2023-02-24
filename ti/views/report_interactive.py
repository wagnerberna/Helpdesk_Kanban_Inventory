from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ti.service.check_user_access import check_user_access


@login_required
def report_interactive(request):
    try:
        check_access = check_user_access(request)
        if not check_access:
            return redirect("access_denied")

        template_path = "ti/pages/report_interactive.html"
        return render(request, template_path)
    except Exception as error:
        print("Internal error:", error)
        raise
