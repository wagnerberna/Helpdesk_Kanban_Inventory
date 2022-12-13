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


# extender user admin
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "user_profile"

    def __str__(self):
        return "%s" % (self.name)


# extender user admin
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s" % (self.user)
