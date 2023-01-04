import base64
import io

import matplotlib
import seaborn as sns

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Gráfico em barra vertical
def make_graphic_bar(title, color, labels, data):
    plt.bar(labels, data, color=color)

    sns.set_theme()
    # sns.despine()
    # sns.set(style="whitegrid")
    # sns.set_color_codes("pastel")
    # sns.despine(left=True, bottom=True)
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
    plt.rcParams["font.size"] = "14"
    plt.grid(color="#95a5a6", linestyle="--", linewidth=2, axis="x", alpha=0.7)

    fig = plt.gcf()
    fig.set_size_inches(20, 4, forward=True)
    # fig.set_dpi(100)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plt.close()
    return string


# Gráfico em barra Pizza
# autopct (número de casas após a vírgula)
def make_graphic_pie(labels, data):
    explode = [0.2, 0, 0, 0, 0]
    colors = ["blue", "green", "yellow", "red", "black"]
    plt.pie(
        data,
        labels=labels,
        # radius=2,
        autopct="%0.0f%%",
        pctdistance=1.1,
        labeldistance=1.2,
        colors=colors,
        explode=explode,
        radius=1,
        shadow=True,
        counterclock=False,
        startangle=90,
    )

    # plt.title(title)
    plt.rcParams["font.size"] = "8"

    fig = plt.gcf()
    # fig.set_size_inches(18, 4, forward=True)
    # fig.set_dpi(100)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plt.close()
    return string
