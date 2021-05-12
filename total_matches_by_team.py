import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def abbreviate_team_name(name):
    '''making abbreviation names'''
    split_name = name.split(' ')
    short_name = [each[0] for each in split_name]
    return ''.join(short_name)


def plot():
    '''Plotting stacked bar graph for
    total matches played by team by season'''

    teams = defaultdict(lambda: defaultdict(int))
    season = set()

    '''creating a dictionay of teams to a dictionay of
       seasons with numbers of matches played'''
    with open('matches.csv', 'r') as file:
        matches = csv.DictReader(file)
        for row in matches:
            teams[abbreviate_team_name(row['team1'])][row['season']] += 1
            teams[abbreviate_team_name(row['team2'])][row['season']] += 1
            season.add(int(row['season']))
        season = sorted(list(season))

    ''' initializing total matches as zero
        in non played season to all teams'''
    for row in teams.keys():
        for col in list(season):
            teams[row][str(col)] = teams[row][str(col)]
        teams[row] = dict(sorted(teams[row].items(),
                          key=lambda x: (x[0], x[1])))

    s_m = []
    team = list(teams.keys())
    for row in teams.items():
        t = []
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
    for a, b in zip(season, b_m[12]):
        plt.text(-0.25+a, 2+b, str(b))

    color = ['orange', 'red', 'blue', 'pink', 'darkblue', 'purple', 'black',
             'green', 'yellow', 'cyan', 'grey', 'peru', 'royalblue']
    plt.bar(season, s_m[0], 0.4, tick_label=season,
            color=color[0], label=team[0])
    for i, row in enumerate(s_m[1:]):
        plt.bar(season, row, 0.4, bottom=b_m[i], color=color[i+1],
                label=team[i+1])

    plt.xlabel('Season')
    plt.ylabel('Matches Played by Team')
    plt.legend()
    plt.title('Matches Played by Team by Season')
    plt.show()


if __name__ == "__main__":
    plot()
