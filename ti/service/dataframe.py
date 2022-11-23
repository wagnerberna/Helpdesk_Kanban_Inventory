import json

import pandas


def open_excel_dataframe(path_file):
    try:
        df = pandas.read_excel(path_file)
        # print(df)
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


def dataframe_desktop_ranking(path_file):
    try:
        df = pandas.read_excel(path_file)
        # print(df)
        ranking_count_values = df["Ranking"].value_counts()
        ranking_count_values = ranking_count_values.sort_index()

        ranking_a = ranking_count_values.get("A")
        ranking_b = ranking_count_values.get("B")
        ranking_c = ranking_count_values.get("C")
        ranking_d = ranking_count_values.get("D")
        ranking_e = ranking_count_values.get("E")

        ranking_values = [ranking_a, ranking_b, ranking_c, ranking_d, ranking_e]

        print(ranking_count_values)
        print(ranking_values)
        # json_records = ranking_count_values.reset_index().to_dict(orient="records")
        # print("type df:::", type(df))
        # print("type json_records:::", json_records)
        # data = []
        # data = json.loads(json_records)
        # print("type data:::", type(data))
        # print(data)
        return ranking_values

    except Exception as error:
        print("Internal error:", error)
        raise
