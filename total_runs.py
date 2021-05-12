import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def abbreviate_team_name(name):
    '''making abbreviation names'''
    split_name = name.split(' ')
    short_name = [each[0] for each in split_name]
    return ''.join(short_name)


def plot():
    '''Plotting bar graph for total
       runs scored by each team'''

    # creating a dictionary of team and their score
    total_run = defaultdict(int)
    with open('deliveries.csv', 'r') as file:
        deliveries = csv.DictReader(file)
        for row in deliveries:
            total_run[abbreviate_team_name
                      (row['batting_team'])] += int(row['total_runs'])

    color = []
    team = list(total_run.keys())
    run = list(total_run.values())

    for col in run:
        if col <= 10000:
            color.append('red')
        elif 10000 < col < 20000:
            color.append('blue')
        else:
            color.append('green')

    # plotting graph
    left = list(range(1, len(team)+1))
    for a, b in zip(left, run):
        plt.text(-0.25+a, 125+b, str(b))

    plt.bar(left, run, tick_label=team, width=0.8, color=color)
    plt.xlabel('Team')
    plt.ylabel('Total Runs Scored')
    plt.title('Run status')
    plt.show()


if __name__ == "__main__":
    plot()
