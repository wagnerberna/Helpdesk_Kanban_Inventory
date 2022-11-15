from django.contrib.auth.models import User
from django.db import models


class RestrictedArea(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = "ti_restricted_area"

    def __str__(self):
        return "%s" % self.user
