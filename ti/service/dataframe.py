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


# def dataframe_department_ranking(path_file):
#     try:
#         df = pandas.read_excel(path_file)
#         df.drop(
#             columns=[
#                 "Usuario",
#                 "Computador",
#                 "Tipo",
#                 "Fabricante",
#                 "CPU_Modelo",
#                 "CPU_Fabricante",
#                 "CPU_Geracao",
#                 "CPU_Descricao",
#                 "Memoria",
#                 "HD",
#                 "SO",
#                 "SO_bits",
#                 "Fabricante",
#                 "Modelo",
#                 "Serial",
#             ],
#             inplace=True,
#         )

#         # print(df)

#         departments = [
#             "Comercial",
#             "Engenharia",
#             "Direcao",
#             "Controladoria",
#             "Fiscal",
#             "Contabilidade",
#             "Financeiro",
#             "TI",
#             "RH",
#             "Marketing",
#             "Juridico",
#             "Zeladoria",
#             "SESMT",
#             "Qualidade",
#             "Ferramentaria",
#             "Fundidos",
#             "Almoxarifado",
#             "Compras",
#             "Lideres",
#             "PCP",
#             "Bobinagem",
#             "Expedicao",
#             "Industrial",
#             "Montagem",
#             "Manutencao",
#         ]

#         df_departments = df.loc[df["Setor"].isin(departments)]
#         # print(df_departments)

#         df_grouped = df_departments.groupby(["Setor", "Ranking"])["Ranking"].count()
#         print("Ponto 0!!!")
#         print(df_grouped)

#         for df in df_grouped:
#             print(df)

#         # ranking_list = df_grouped.values.tolist()
#         # print(ranking_list)

#         # ranking_departament = []

#         # departament_count_values = df["Setor"].value_counts()
#         # print("departament_count_values:::", departament_count_values)
#         # department_values = departament_count_values.sort_index()
#         # print("department_values:::", department_values)

#         # for departament in departments:

#         #     department_count = department_values.get(departament)

#         #     ranking_departament.append(department_count)

#         return ranking_list

#     except Exception as error:
#         print("Internal error:", error)
#         raise
