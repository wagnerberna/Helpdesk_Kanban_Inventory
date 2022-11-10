import base64
import io

import matplotlib.pyplot as plot


# Gráfico em barra vertical
def make_graphic_bar(title, color, techinicals, total_per_techinical):
    plot.bar(techinicals, total_per_techinical, color=color)

    plot.title(title)
    fig = plot.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plot.close()
    return string


# Gráfico em barra horizontal
def make_graphic_barh(title, color, techinicals, total_per_techinical):
    plot.barh(techinicals, total_per_techinical, color=color)

    plot.title(title)
    fig = plot.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plot.close()
    return string
