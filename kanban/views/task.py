from django.contrib.auth.decorators import login_required

from kanban.models import Task
from kanban.service.check_user_access import check_user_access
