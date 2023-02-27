import json

import pandas


def excel_to_dataframe(path_file):
    try:
        df = pandas.read_excel(path_file)
        return df

    except Exception as error:
        print("Internal error:", error)
        raise


def excel_to_json(path_file):
    try:
        df = pandas.read_excel(path_file)
        json_records = df.reset_index().to_json(orient="records")
        data = []
        data = json.loads(json_records)
        return data

    except Exception as error:
        print("Internal error:", error)
        raise


def dataframe_desktop_ranking(path_file):
    try:
        df = pandas.read_excel(path_file)
        ranking_count_values = df["Ranking"].value_counts()
        ranking_count_values = ranking_count_values.sort_index()

        ranking_a = ranking_count_values.get("A")
        ranking_b = ranking_count_values.get("B")
        ranking_c = ranking_count_values.get("C")
        ranking_d = ranking_count_values.get("D")
        ranking_e = ranking_count_values.get("E")
        ranking_values = [
            int(ranking_a),
            int(ranking_b),
            int(ranking_c),
            int(ranking_d),
            int(ranking_e),
        ]
        # print(ranking_values)

        return ranking_values

    except Exception as error:
        print("Internal error:", error)
        raise
