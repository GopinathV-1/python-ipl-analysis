import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def plot():
    '''Plotting bar graph for
       count of foreign umpires'''
    umpire = []
    # converting csv file to list
    with open('umpires.csv', 'r') as file:
        umpire = list(csv.reader(file))
    foreign_umpire = defaultdict(str)
    # counting umpires based on origin of country
    for row in umpire[1:]:
        if row[1].strip() == 'India':
            continue
        foreign_umpire[row[0].strip()] = row[1].strip()
    umpire_count = defaultdict(int)
    for row in foreign_umpire.items():
        umpire_count[row[1]] += 1
    ump_country, ump_count, color = [], [], []
    for row in umpire_count.items():
        ump_country.append(row[0])
        ump_count.append(row[1])
    left = range(1, len(ump_count)+1)
    for row in range(len(ump_country)):
        if ump_count[row] <= 2:
            color.append('red')
        elif ump_count[row] > 2 and ump_count[row] < 5:
            color.append('blue')
        else:
            color.append('green')
    # plotting bar graph
    plt.bar(left, ump_count, tick_label=ump_country, width=0.8, color=color)
    for a, b in zip(left, ump_count):
        plt.text(-0.15+a, 0.1+b, str(b))
    plt.xlabel('Country')
    plt.ylabel('Umpire\'s count')
    plt.title('Foreign Umpire Analysis')
    plt.show()


if __name__ == "__main__":
    plot()
