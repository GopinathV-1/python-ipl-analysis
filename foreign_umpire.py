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
    foreign_umpire_country_count = Counter(umpire_country)
    foreign_umpire_country_origin = list(foreign_umpire_country_count.keys())
    umpire_count = list(foreign_umpire_country_count.values())
    color = []

    for row in umpire_count:
        if row <= 2:
            color.append('red')
        elif 2 < row < 5:
            color.append('blue')
        else:
            color.append('green')

    # plotting bar graph
    graph_length = range(1, len(umpire_count)+1)
    for a, b in zip(graph_length, umpire_count):
        plt.text(-0.15+a, 0.1+b, str(b))

    plt.bar(graph_length, umpire_count,
            tick_label=foreign_umpire_country_origin,
            width=0.8, color=color)
    plt.xlabel('Country')
    plt.ylabel('Umpire\'s count')
    plt.title('Foreign Umpire Analysis')
    plt.show()


if __name__ == "__main__":
    plot()
