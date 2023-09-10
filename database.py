import csv


def get_data() -> list:
    data = []
    with open("prices.csv", newline="", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            data.append(row)
    return data
