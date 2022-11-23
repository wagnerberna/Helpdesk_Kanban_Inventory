import base64
import io

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Gráfico em barra vertical
def make_graphic_bar(title, color, labels, data):
    plt.bar(labels, data, color=color)

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
def make_graphic_barh(title, color, labels, data):
    plt.barh(labels, data, color=color)

    plt.title(title)
    plt.rcParams["font.size"] = "18"

    fig = plt.gcf()
    fig.set_size_inches(18, 4, forward=True)
    fig.set_dpi(100)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plt.close()
    return string


# Gráfico em barra Pizza
def make_graphic_pie(title, labels, data):
    plt.pie(data, labels=labels)

    plt.title(title)
    plt.rcParams["font.size"] = "18"

    fig = plt.gcf()
    fig.set_size_inches(18, 4, forward=True)
    fig.set_dpi(100)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plt.close()
    return string
