import csv


def get_data() -> None:
    with open("prices.csv", newline="", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        print(csvreader)
        for row in csvreader:
            print(row)
