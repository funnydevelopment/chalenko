import csv


def get_data() -> list:
    data = []
    with open("prices.csv", newline="", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        print(csvreader)
        for row in csvreader:
            data.append(row)
    return data


def get_data_2() -> None:
    with open("prices.csv", newline="", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        print(csvreader)
        for row in csvreader:
            print(row)
