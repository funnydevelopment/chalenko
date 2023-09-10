import pprint

import database
import views


if __name__ == "__main__":
    data = database.get_data()
    plot_datas = views.create_plot_datas(data)
    pprint.pprint(type(plot_datas[0]["open_date"]))
    # views.create_plot_from_datas(plot_datas)
