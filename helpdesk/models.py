from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Support(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True
        db_table = "helpdesk_support"

    def __str__(self):
        return "%s" % (self.user_name)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True
        db_table = "helpdesk_category"

    def __str__(self):
        return self.name


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True
        db_table = "helpdesk_status"

    def __str__(self):
        return self.name


class Demand(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=70, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="demand_images", null=True, blank=True)
    attendant = models.ForeignKey(
        Support, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    solution = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        managed = True
        db_table = "helpdesk_demand"

    def __str__(self):
        return "Solicitação: %s / Descrição: %s" % (self.user_name, self.description)
