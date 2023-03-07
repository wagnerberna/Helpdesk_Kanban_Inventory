from django.contrib.auth.models import User
from django.db import models
from ti.models import Department


# Hardware
class WorkstationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_workstation_type"

    def __str__(self):
        return "%s" % (self.name)


class WorkstationManufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_workstation_manufacturer"

    def __str__(self):
        return "%s" % (self.name)


class WorkstationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_workstation_model"

    def __str__(self):
        return "%s" % (self.name)


class CpuManufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_cpu_manufacturer"

    def __str__(self):
        return "%s" % (self.name)


class CpuModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_cpu_model"

    def __str__(self):
        return "%s" % (self.name)


class CpuGeneration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_cpu_generation"

    def __str__(self):
        return "%s" % (self.name)


class CpuDescription(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_cpu_description"

    def __str__(self):
        return "%s" % (self.name)


class MemorySize(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_memory_size"

    def __str__(self):
        return "%s" % (self.size)


class HardDiskSize(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_hard_disk_size"

    def __str__(self):
        return "%s" % (self.size)


# class MetricUnit(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Ranking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    description = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_ranking"

    def __str__(self):
        return "%s" % (self.name)


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
    workstation_serial = models.CharField(max_length=25, null=True, unique=True)
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
    # hard_disk_unit = models.ForeignKey(MetricUnit, on_delete=models.CASCADE, null=True)
    memory_size = models.ForeignKey(MemorySize, on_delete=models.CASCADE, null=True)
    # memory_unit = models.ForeignKey(MetricUnit, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Software
class OperationalSystem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_operational_system"

    def __str__(self):
        return "%s" % (self.name)


class SystemArchitecture(models.Model):
    id = models.AutoField(primary_key=True)
    architecture = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_system_architecture"

    def __str__(self):
        return "%s" % (self.architecture)


class Software(models.Model):
    id = models.AutoField(primary_key=True)
    operating_system = models.ForeignKey(
        OperationalSystem, on_delete=models.CASCADE, null=True
    )
    architecture = models.ForeignKey(
        SystemArchitecture, on_delete=models.CASCADE, null=True
    )
    # architecture_unit = models.ForeignKey(
    #     MetricUnit, on_delete=models.CASCADE, null=True
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_software"

    def __str__(self):
        return "%s %s" % (self.operating_system, self.architecture)


# Inventory - NF
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_invoice"

    def __str__(self):
        return "%s" % (self.number)


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    inventory = models.IntegerField(null=True, unique=True)
    hostname = models.CharField(max_length=20, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    ranking = models.ForeignKey(Ranking, on_delete=models.CASCADE, null=True)
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE, null=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_iventory"

    def __str__(self):
        return "%s" % (self.hostname)
