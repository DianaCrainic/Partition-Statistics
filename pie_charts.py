from cutecharts.charts import Pie
from cutecharts.components import Page


def pie_radius():
    chart = Pie("Number of extension files ")
    chart.set_options(labels=['exe', 'ini', 'jpg', 'mp3', 'png', 'txt', 'zip'], inner_radius=0)
    chart.add_series([3, 1, 21, 2, 1, 1, 3])
    return chart


page = Page()
page.add(pie_radius())
page.render()
