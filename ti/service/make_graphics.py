import base64
import io

import matplotlib
import seaborn as sns

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Gráfico em barra vertical
# theme: darkgrid, whitegrid, dark, white, ticks
# context: notebook, paper, talk, poster


class MakeGraphics:
    def bar(self, title, color, labels, data):
        plt.bar(labels, data, color=color)

        sns.set_theme()
        sns.despine()
        sns.set_context("talk")

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
    def bar_ranking(self, title, xlabel, ylabel, df):
        plt.figure(figsize=(17, 7))
        sns.countplot(
            x="Setor",
            hue="Ranking",
            data=df,
            palette={
                "A": "#86cbf9",
                "B": "#7fe686",
                "C": "#ffe97f",
                "D": "#fe7167",
                "E": "#ff80ff",
            },
            hue_order=["A", "B", "C", "D", "E"],
        )
        sns.set_theme()
        sns.despine()
        sns.set_context("talk")

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read())
        plt.close()
        return string

    # Gráfico em barra vertical de grupos
    def bar_project(self, title, xlabel, ylabel, df):
        plt.figure(figsize=(38, 10))
        sns.countplot(
            x="project__name",
            hue="status__name",
            data=df,
            palette={
                "TO DO": "#7fe686",
                "DOING": "#ffe97f",
                "BLOCKED": "#fe7167",
                "DONE": "#86cbf9",
            },
            hue_order=["TO DO", "DOING", "BLOCKED", "DONE"],
        )
        sns.set_theme()
        sns.despine()
        sns.set_context("poster")
        # sns.set_theme(font_scale=3.5)
        # sns.set(font_scale=1)

        plt.title(title, fontsize=35)
        plt.xlabel(xlabel, fontsize=25)
        plt.ylabel(ylabel, fontsize=25)
        plt.legend(
            title="Status",
            loc="upper left",
            labels=["TO DO", "DOING", "BLOCKED", "DONE"],
        )
        # plt.tick_params(labelsize=20)

        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read())
        plt.close()
        return string

    # Gráfico em barra horizontal
    def barh(self, title, color, labels, data):
        plt.barh(labels, data, color=color)

        sns.set_theme()
        sns.despine()
        plt.title(title, fontsize=35)
        sns.set_context("talk")

        # plt.rcParams["font.size"] = "16"
        # plt.grid(color="#95a5a6", linestyle="--", linewidth=2, axis="x", alpha=0.7)

        fig = plt.gcf()
        fig.set_size_inches(32, 7)
        # fig.set_dpi(100)
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read())
        plt.close()
        return string

    # Gráfico em barra Pizza
    # autopct (número de casas após a vírgula)
    def pie_ranking(self, labels, data):
        explode = [0.2, 0, 0, 0, 0]
        colors = ["#86cbf9", "#7fe686", "#ffe97f", "#fe7167", "#ff80ff"]

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
