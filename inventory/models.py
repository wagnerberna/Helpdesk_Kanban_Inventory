# from django.contrib.auth.models import User
# from django.db import models
# from ti.models import Department


# class CpuManufacturer(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=15, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class CpuModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=15, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Cpu(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=15, null=True)
#     manufacturer = models.ForeignKey(CpuManufacturer, on_delete=models.CASCADE, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class ComputerManufacturer(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=15, null=True)

# class SystemOperation(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=15, null=True)

# class Computer(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=15, null=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# cpu_generation
# cpu_description
# memory
# hard_disk
