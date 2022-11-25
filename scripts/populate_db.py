import json

import pandas
from kanban.models import Category, Project, Status, Task, Team


def run():
    try:
        path_file = "doc/projects_names.xlsx"
        df = pandas.read_excel(path_file)
        print(df)
        json_records = df.reset_index().to_json(orient="records")
        # print("type df:::", type(df))
        # print("type json_records:::", type(json_records))
        data = []
        data = json.loads(json_records)
        # print("type data:::", type(data))
        # print(data)
        return data

    except Exception as error:
        print("Internal error:", error)
        raise
