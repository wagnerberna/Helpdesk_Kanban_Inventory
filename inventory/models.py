from django.contrib.auth.models import User
from django.db import models
from ti.models import Department


# NF
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    name = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CpuModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CpuGeneration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CpuDescription(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
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
    name = models.CharField(max_length=5, null=True)
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
class OperatingSystem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class version


