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
    team_name = list(total_run.keys())
    runs_scored = list(total_run.values())

    for col in runs_scored:
        if col <= 10000:
            color.append('red')
        elif 10000 < col < 20000:
            color.append('blue')
        else:
            color.append('green')

    # plotting graph
    graph_length = list(range(1, len(team_name)+1))
    for a, b in zip(graph_length, runs_scored):
        plt.text(-0.25+a, 125+b, str(b))

    plt.bar(graph_length, runs_scored, tick_label=team_name,
            width=0.8, color=color)
    plt.xlabel('Team')
    plt.ylabel('Total Runs Scored')
    plt.title('Run status')
    plt.show()


if __name__ == "__main__":
    plot()
