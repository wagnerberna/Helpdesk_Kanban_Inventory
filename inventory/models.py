from django.contrib.auth.models import User
from django.db import models
from ti.models import Department


# Hardware
class WorkstationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WorkstationManufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WorkstationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CpuManufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CpuModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CpuGeneration(models.Model):
    id = models.AutoField(primary_key=True)
    generation = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CpuDescription(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MemorySize(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HardDiskSize(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MetricUnit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ranking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5, null=True)
    description = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hardware(models.Model):
    id = models.AutoField(primary_key=True)
    workstation_type = models.ForeignKey(
        WorkstationType, on_delete=models.CASCADE, null=True
    )
    workstation_manufacturer = models.ForeignKey(
        WorkstationManufacturer, on_delete=models.CASCADE, null=True
    )
    workstation_model = models.ForeignKey(
        WorkstationModel, on_delete=models.CASCADE, null=True
    )
    workstation_serial = models.CharField(max_length=25, null=True)
    cpu_manufacturer = models.ForeignKey(
        CpuManufacturer, on_delete=models.CASCADE, null=True
    )
    cpu_model = models.ForeignKey(CpuModel, on_delete=models.CASCADE, null=True)
    cpu_generation = models.ForeignKey(
        CpuGeneration, on_delete=models.CASCADE, null=True
    )
    cpu_description = models.ForeignKey(
        CpuDescription, on_delete=models.CASCADE, null=True
    )
    hard_disk_size = models.ForeignKey(
        HardDiskSize, on_delete=models.CASCADE, null=True
    )
    hard_disk_unit = models.ForeignKey(MetricUnit, on_delete=models.CASCADE, null=True)
    memory_size = models.ForeignKey(MemorySize, on_delete=models.CASCADE, null=True)
    memory_unit = models.ForeignKey(MetricUnit, on_delete=models.CASCADE, null=True)
    ranking = models.ForeignKey(Ranking, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Software
class OperationalSystem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SystemArchitecture(models.Model):
    id = models.AutoField(primary_key=True)
    architecture = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Software(models.Model):
    id = models.AutoField(primary_key=True)
    operating_system = models.ForeignKey(
        OperationalSystem, on_delete=models.CASCADE, null=True
    )
    architecture = models.ForeignKey(
        SystemArchitecture, on_delete=models.CASCADE, null=True
    )
    architecture_unit = models.ForeignKey(
        MetricUnit, on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Inventory - NF
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    inventory = models.IntegerField(null=True)
    hostname = models.CharField(max_length=20, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE, null=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
