from django.contrib import admin

from inventory.models import (
    CpuDescription,
    CpuGeneration,
    CpuManufacturer,
    CpuModel,
    HardDiskSize,
    Hardware,
    Inventory,
    Invoice,
    MemorySize,
    OperationalSystem,
    OperationalSystemVersion,
    Ranking,
    Software,
    StatusSituation,
    SystemArchitecture,
    WorkstationManufacturer,
    WorkstationModel,
    WorkstationType,
    ServerStatus,
    Server
)

# Register your models here.
admin.site.register(CpuDescription)
admin.site.register(CpuGeneration)
admin.site.register(CpuManufacturer)
admin.site.register(CpuModel)
admin.site.register(HardDiskSize)
admin.site.register(Hardware)
admin.site.register(Inventory)
admin.site.register(Invoice)
admin.site.register(MemorySize)
admin.site.register(OperationalSystem)
admin.site.register(OperationalSystemVersion)
admin.site.register(Ranking)
admin.site.register(Software)
admin.site.register(SystemArchitecture)
admin.site.register(WorkstationManufacturer)
admin.site.register(WorkstationModel)
admin.site.register(WorkstationType)
admin.site.register(StatusSituation)
admin.site.register(ServerStatus)
admin.site.register(Server)
