import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def plot():
    '''Plotting stacked bar graph for
    total matches played by team by season'''
    def short(name):
        '''making abbreviation names'''
        split_name = name.split(' ')
        short_name = [each[0] for each in split_name]
        return ''.join(short_name)
    matches = []
    # converting csv files to list
    with open('matches.csv', 'r') as file:
        matches = list(csv.reader(file))
    # calculating total matches in a season by a team
    teams = defaultdict(str)
    for row in matches[1:]:
        teams[short(row[4])] = defaultdict(str)
        teams[short(row[5])] = defaultdict(str)
    left = list(range(2008, 2018))
    for row in teams.keys():
        for col in left:
            teams[row][str(col)] = 0
    for row in matches[1:]:
        teams[short(row[4])][row[1]] += 1
        teams[short(row[5])][row[1]] += 1
    s_m, team = [], []
    for row in teams.items():
        t = []
        team.append(row[0])
        for col in row[1].items():
            t.append(col[1])
        s_m.append(t)
    b_m = []
    for i, row in enumerate(s_m):
        L = []
        for j, col in enumerate(row):
            if i == 0:
                L.append(col)
            else:
                L.append(b_m[i-1][j] + col)
        b_m.append(L)
    # plotting stacked bar graph
    color = ['orange', 'red', 'blue', 'pink', 'darkblue', 'purple', 'black',
             'green', 'yellow', 'cyan', 'grey', 'peru', 'royalblue']
    plt.bar(left, s_m[0], 0.4, tick_label=left, color=color[0], label=team[0])
    for i, row in enumerate(s_m[1:]):
        plt.bar(left, row, 0.4, bottom=b_m[i], color=color[i+1],
                label=team[i+1])
    for a, b in zip(left, b_m[12]):
        plt.text(-0.25+a, 2+b, str(b))
    plt.xlabel('Season')
    plt.ylabel('Matches Played by Team')
    plt.legend()
    plt.title('Matches Played by Team by Season')
    plt.show()


if __name__ == "__main__":
    plot()
