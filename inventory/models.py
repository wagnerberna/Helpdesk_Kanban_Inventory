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
        WorkstationManufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    workstation_model = models.ForeignKey(
        WorkstationModel, on_delete=models.CASCADE, null=True, blank=True
    )
    cpu_manufacturer = models.ForeignKey(
        CpuManufacturer, on_delete=models.CASCADE, null=True
    )
    cpu_model = models.ForeignKey(CpuModel, on_delete=models.CASCADE, null=True)
    cpu_generation = models.ForeignKey(
        CpuGeneration, on_delete=models.CASCADE, null=True, blank=True
    )
    cpu_description = models.ForeignKey(
        CpuDescription, on_delete=models.CASCADE, null=True
    )
    hard_disk_size = models.ForeignKey(
        HardDiskSize, on_delete=models.CASCADE, null=True
    )
    memory_size = models.ForeignKey(MemorySize, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_hardware"
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "workstation_type",
                    "workstation_manufacturer",
                    "cpu_manufacturer",
                    "cpu_model",
                    "cpu_generation",
                    "hard_disk_size",
                    "memory_size",
                    "workstation_model",
                ],
                name="unique_hardware_group",
            )
        ]

    def __str__(self):
        return "%s -%s -%s %s %s -HD:%s -Mem:%s -Modelo:%s" % (
            self.workstation_type,
            self.workstation_manufacturer,
            self.cpu_manufacturer,
            self.cpu_model,
            self.cpu_generation,
            self.hard_disk_size,
            self.memory_size,
            self.workstation_model,
        )


# Software
class OperationalSystem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_operational_system"

    def __str__(self):
        return "%s" % (self.name)


class OperationalSystemVersion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_operational_system_version"

    def __str__(self):
        return "%s" % (self.name)


class SystemArchitecture(models.Model):
    id = models.AutoField(primary_key=True)
    architecture = models.CharField(max_length=20, null=True, unique=True, blank=True)
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
    operating_system_version = models.ForeignKey(
        OperationalSystemVersion, on_delete=models.CASCADE, null=True
    )
    architecture = models.ForeignKey(
        SystemArchitecture, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_software"
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "operating_system",
                    "operating_system_version",
                    "architecture",
                ],
                name="unique_software_group",
            )
        ]

    def __str__(self):
        return "%s %s %s" % (
            self.operating_system,
            self.operating_system_version,
            self.architecture,
        )


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


class StatusSituation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)

    class Meta:
        managed = True
        db_table = "inventory_status_situation"

    def __str__(self):
        return "%s" % (self.name)


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    inventory = models.IntegerField(null=True, unique=True)
    hostname = models.CharField(max_length=20, null=True, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True
    )
    ranking = models.ForeignKey(
        Ranking, on_delete=models.CASCADE, null=True, blank=True
    )
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE, null=True)
    workstation_serial = models.CharField(
        max_length=25, null=True, unique=True, blank=True
    )
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.ForeignKey(StatusSituation, on_delete=models.CASCADE, null=True)
    detail = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory"

    def __str__(self):
        return "%s : %s" % (self.inventory, self.hostname)


class ServerStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)

    class Meta:
        managed = True
        db_table = "inventory_server_status"

    def __str__(self):
        return "%s" % (self.name)


class Server(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=20, null=True, unique=True, blank=True)
    ip = models.CharField(max_length=15, null=True, blank=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(ServerStatus, on_delete=models.CASCADE, null=True)
    serviceRun = models.CharField(max_length=80, null=True, blank=True)
    url_internal = models.CharField(max_length=120, null=True, blank=True)
    url_external = models.CharField(max_length=120, null=True, blank=True)
    detail = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_server"

    def __str__(self):
        return "%s" % (self.hostname)


class SwitchManufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_switch_manufacturer"

    def __str__(self):
        return "%s" % (self.name)


class SwitchModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_switch_model"

    def __str__(self):
        return "%s" % (self.name)


class SwitchHardware(models.Model):
    id = models.AutoField(primary_key=True)
    manufacturer = models.ForeignKey(
        SwitchManufacturer, on_delete=models.CASCADE, null=True
    )
    model = models.ForeignKey(SwitchModel, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_switch_hardware"
        constraints = [
            models.UniqueConstraint(
                fields=["manufacturer", "model"], name="unique_switch_group"
            )
        ]

    def __str__(self):
        return "%s - %s" % (self.manufacturer, self.model)


class Switch(models.Model):
    def image_upload(self, filename):
        return "switch_image/" + "Switch - " + str(self.inventory)

    id = models.AutoField(primary_key=True)
    inventory = models.IntegerField(null=True, blank=True, unique=True)
    user = models.CharField(max_length=15, null=True, unique=False, blank=True)
    password = models.CharField(max_length=15, null=True, unique=False, blank=True)
    ip = models.CharField(max_length=15, null=True, blank=True, unique=False)
    stack = models.BooleanField(default=False)
    switch_hardware = models.ForeignKey(
        SwitchHardware, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.ForeignKey(StatusSituation, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True
    )
    url_access = models.CharField(max_length=30, null=True, blank=True)
    mac = models.CharField(max_length=17, null=True, blank=True)
    detail = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=image_upload, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "inventory_switch"

    def __str__(self):
        return "%s - %s" % (self.switch_hardware, self.ip)
