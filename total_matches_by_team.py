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

    team_seasonal_matches = defaultdict(lambda: defaultdict(int))
    season = set()

    '''creating a dictionay of teams to a dictionay of
       seasons with numbers of matches played'''
    with open('matches.csv', 'r') as file:
        matches = csv.DictReader(file)
        for row in matches:
            team_seasonal_matches[abbreviate_team_name(
                                  row['team1'])][row['season']] += 1
            team_seasonal_matches[abbreviate_team_name(
                                  row['team2'])][row['season']] += 1
            season.add(int(row['season']))
        season = sorted(list(season))

    ''' initializing total matches as zero
        in non played season to all teams'''
    for row in team_seasonal_matches.keys():
        for col in list(season):
            team_seasonal_matches[row][str(col)] = (team_seasonal_matches
                                                    [row][str(col)])
        team_seasonal_matches[row] = dict(sorted(team_seasonal_matches
                                          [row].items(),
                                          key=lambda x: (x[0], x[1])))

    matches_matrix = []
    team_names = list(team_seasonal_matches.keys())
    for row in team_seasonal_matches.items():
        temporary_list = []
        for col in row[1].items():
            temporary_list.append(col[1])
        matches_matrix.append(temporary_list)

    prefix_sum_matrix = []
    for index, row in enumerate(matches_matrix):
        temporary_list = []
        for j_index, col in enumerate(row):
            if index == 0:
                temporary_list.append(col)
            else:
                temporary_list.append(prefix_sum_matrix
                                      [index-1][j_index] + col)
        prefix_sum_matrix.append(temporary_list)

    # plotting stacked bar graph
    for a, b in zip(season, prefix_sum_matrix[12]):
        plt.text(-0.25+a, 2+b, str(b))

    color = ['orange', 'red', 'blue', 'pink', 'darkblue', 'purple', 'black',
             'green', 'yellow', 'cyan', 'grey', 'peru', 'royalblue']
    plt.bar(season, matches_matrix[0], 0.4, tick_label=season,
            color=color[0], label=team_names[0])
    for i, row in enumerate(matches_matrix[1:]):
        plt.bar(season, row, 0.4, bottom=prefix_sum_matrix[i],
                color=color[i+1], label=team_names[i+1])

    plt.xlabel('Season')
    plt.ylabel('Matches Played by Team')
    plt.legend()
    plt.title('Matches Played by Team by Season')
    plt.show()


if __name__ == "__main__":
    plot()
