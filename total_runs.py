import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def plot():
    '''Plotting bar graph for total
       runs scored by each team'''
    def short(name):
        '''making abbreviation names'''
        split_name = name.split(' ')
        short_name = [each[0] for each in split_name]
        return ''.join(short_name)
    deliveries = []
    # converting csv file to list
    with open('deliveries.csv', 'r') as file:
        deliveries = list(csv.reader(file))
    total_run = defaultdict(int)
    for row in deliveries[1:]:
        total_run[short(row[2])] += int(row[17])
    team, run, color = [], [], []
    for row in total_run.items():
        team.append(row[0])
        run.append(row[1])
    for col in run:
        if col <= 10000:
            color.append('red')
        elif col > 10000 and col < 20000:
            color.append('blue')
        else:
            color.append('green')
    left = list(range(1, len(team)+1))
    # plotting graph
    plt.bar(left, run, tick_label=team, width=0.8, color=color)
    for a, b in zip(left, run):
        plt.text(-0.25+a, 125+b, str(b))
    plt.xlabel('Team')
    plt.ylabel('Total Runs Scored')
    plt.title('Run status')
    plt.show()


if __name__ == "__main__":
    plot()
