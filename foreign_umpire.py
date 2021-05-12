import csv
import matplotlib.pyplot as plt
from collections import Counter


def plot():
    '''Plotting bar graph for
       count of foreign umpires'''

    umpire_country = []
    with open('umpires.csv', 'r') as file:
        umpire = csv.DictReader(file)
        for row in umpire:
            if row[' country'] != ' India':
                umpire_country.append(row[' country'].strip())

    # creating a dictionary of foreign umpire country and their count
    umpire_country_count = Counter(umpire_country)
    ump_country = list(umpire_country_count.keys())
    ump_count = list(umpire_country_count.values())
    color = []

    for row in range(len(ump_country)):
        if ump_count[row] <= 2:
            color.append('red')
        elif 2 < ump_count[row] < 5:
            color.append('blue')
        else:
            color.append('green')

    # plotting bar graph
    left = range(1, len(ump_count)+1)
    for a, b in zip(left, ump_count):
        plt.text(-0.15+a, 0.1+b, str(b))

    plt.bar(left, ump_count, tick_label=ump_country, width=0.8, color=color)
    plt.xlabel('Country')
    plt.ylabel('Umpire\'s count')
    plt.title('Foreign Umpire Analysis')
    plt.show()


if __name__ == "__main__":
    plot()
