import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import csv


def parse(rawFile, delimiter):
    # open CSV
    openedFile = open(rawFile)

    # read CSV
    csvData = csv.reader(openedFile, delimiter=delimiter)

    parsedData = []
    fields = next(csvData)

    # iterates each row, creating new dicts matching fields (first row) with data
    for row in csvData:
        parsedData.append(dict(zip(fields, row)))

    return parsedData


def visualize_days(parsedData):
    counter = Counter(item["DayOfWeek"] for item in parsedData)

    # orders our counter
    data_list = [counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]

    # used for x axis labels
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    plt.plot(data_list)
    plt.xticks(range(len(day_tuple)), day_tuple)

    plt.show()


def visualize_type(parsedData):
    width = 0.5

    counter = Counter(item["Category"] for item in parsedData)

    labels = tuple(counter.keys())

    xlocations = np.arange(len(labels)) + 0.5

    plt.bar(xlocations, counter.values(), width=width)

    plt.xticks(xlocations + width / 20, labels, rotation=90)

    plt.subplots_adjust(bottom=0.5)

    plt.rcParams["figure.figsize"] = 12, 8

    plt.show()


def visualize_resolution(parsedData):
    width = 0.5

    counter = Counter(item["Resolution"] for item in parsedData)
    print(counter)
    labels = tuple(counter.keys())

    xlocations = np.arange(len(labels)) + 0.5

    plt.bar(xlocations, counter.values(), width=width)

    plt.xticks(xlocations + width / 20, labels, rotation=90)

    plt.subplots_adjust(bottom=0.5)

    plt.rcParams["figure.figsize"] = 12, 8

    plt.show()



newData = parse("sample_sfpd_incident_all.csv", ",")
# visualize_days(newData)
# visualize_type(newData)
visualize_resolution(newData)
