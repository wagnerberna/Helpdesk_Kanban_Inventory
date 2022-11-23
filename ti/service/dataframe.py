import json

import pandas


def open_excel_dataframe(path_file):
    try:
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
