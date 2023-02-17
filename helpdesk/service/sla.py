import os
from datetime import datetime


def sla_save(pk, status):
    file_path = f"doc/sla/{pk}.csv"
    # if os.path.isfile(file_path):
    date = datetime.now()
    sla_file = open(file_path, "a+")
    sla_file.write(status)
    sla_file.write(str(date))
    sla_file.close()
