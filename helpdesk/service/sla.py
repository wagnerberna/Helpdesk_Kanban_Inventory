import os
from datetime import datetime

import pandas as pd


def sla_save(pk, status):
    file_path = f"doc/sla/{pk}.csv"
    date = datetime.now()
    data = {"pk": [pk], "status": [status], "date": [date]}
    if os.path.isfile(file_path):
        print("arquivo existe")
        sla_file = pd.read_csv(file_path)
        sla_file.append(data, ignore_index=True, sort=False)

        sla_file.to_csv(file_path)

    else:
        print("arquivo não existe")
        print(data)
        sla_file = pd.DataFrame(data)

        sla_file.to_csv(file_path)
