import base64
import io

import matplotlib
import seaborn as sns

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Gráfico em barra vertical
# theme: darkgrid, whitegrid, dark, white, ticks
# context: notebook, paper, talk, poster
def make_graphic_bar(title, color, labels, data):
    plt.bar(labels, data, color=color)

    sns.set_theme()
    sns.despine()
    sns.set_context("talk")

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


# Gráfico em barra vertical de grupos
def make_graphic_bar_group(title, xlabel, ylabel, df):
    # plt.bar(data)

    plt.figure(figsize=(15, 5))
    sns.countplot(x="Setor", hue="Ranking", data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    sns.set_theme()
    sns.despine()
    sns.set_context("talk")

    # sns.set(style="whitegrid")
    # sns.set_color_codes("pastel")
    # sns.despine(left=True, bottom=True)

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

    sns.set_theme()
    sns.despine()
    sns.set_context("notebook")

    # plt.title(title)
    plt.rcParams["font.size"] = "16"
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

    sns.set_theme()
    sns.despine()
    sns.set_context("notebook")

    plt.pie(
        data,
        labels=labels,
        # radius=2,
        autopct="%0.0f%%",
        pctdistance=1.12,
        labeldistance=1.25,
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
