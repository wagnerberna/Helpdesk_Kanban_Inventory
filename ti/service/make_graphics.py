import base64
import io

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Gráfico em barra vertical
def make_graphic_bar(title, color, techinicals, total_per_techinical):
    plt.bar(techinicals, total_per_techinical, color=color)

    plt.title(title)
    plt.rcParams["font.size"] = "16"
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plt.close()
    return string


# Gráfico em barra horizontal
def make_graphic_barh(title, color, projects_names, project_percent_to_graphic):
    plt.barh(projects_names, project_percent_to_graphic, color=color)

    plt.title(title)
    plt.rcParams["font.size"] = "16"
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plt.close()
    return string
