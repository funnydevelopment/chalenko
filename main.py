import database
import views


if __name__ == "__main__":
    # result = database.get_data_2()
    # print(result)
    print(views.check_data_valid(["2023-07-23 06:35:11.997999872", "1873.3567938612"]))
    print(views.check_data_valid(["2023-07-23 06:q5:11.997999872", "1873.3567938612"]))
    print(views.check_data_valid(["2023-07-23 06:35:s1.997999872", "1873.3567938612"]))
    print(views.check_data_valid(["2023-07-23 a6:35:11.997999872", "1873.3567938612"]))
    print(views.check_data_valid(["2023-07-23 06:35:11.'97999872", "1873.3567938612"]))
    print(views.check_data_valid(["2023-07-[3 06:35:11.997999872", "1873.3567938612"]))
    print(views.check_data_valid(["2023-z7-23 06:35:11.997999872", "1873.3567938612"]))
    print(views.check_data_valid(["2o23-07-23 06:35:11.997999872", "1873.3567938612"]))
    print(views.check_data_valid(["2023-07-23 06:35:11.997999872", "фывыфаы"]))
    print(views.check_data_valid(["invalid_date", "invalid_price"]))
    # views.test_data_plot()
