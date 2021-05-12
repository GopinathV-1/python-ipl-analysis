import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def plot():
    '''Plotting bar graph for top
       run scored RCB batsman'''
    deliveries = []
    # converting csv file to list
    with open('deliveries.csv', 'r') as file:
        deliveries = list(csv.reader(file))
    individual_runs = defaultdict(int)
    for row in deliveries[1:]:
        if row[2] == 'Royal Challengers Bangalore':
            individual_runs[row[6]] += int(row[17])
    individual_runs = dict(sorted(individual_runs.items(),
                                  key=lambda kv: (kv[1], kv[0]), reverse=True))
    batsman, runs, color = [], [], []
    for row in list(individual_runs.items())[:10]:
        batsman.append(row[0])
        runs.append(row[1])
    left = list(range(1, 11))
    for row in range(0, 10):
        if runs[row] <= 1000:
            color.append('red')
        elif runs[row] > 1000 and runs[row] < 2000:
            color.append('blue')
        else:
            color.append('green')
    # plotting bar graph
    plt.bar(left, runs, tick_label=batsman, width=0.8, color=color)
    for a, b in zip(left, runs):
        plt.text(-0.25+a, 25+b, str(b))
    plt.xlabel('Batsman')
    plt.ylabel('Total Runs Scored')
    plt.title('Top RCB Batsman Run status')
    plt.show()


if __name__ == "__main__":
    plot()
