import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def plot():
    '''Plotting bar graph for top
       run scored RCB batsman'''

    # creating dictionary of RCB batsman and their scores
    individual_runs = defaultdict(int)
    with open('deliveries.csv', 'r') as file:
        deliveries = csv.DictReader(file)
        for row in deliveries:
            if row['batting_team'] == 'Royal Challengers Bangalore':
                individual_runs[row['batsman']] += int(row['total_runs'])

    # Descending sort of batsman based on their scores
    individual_runs = dict(sorted(individual_runs.items(),
                                  key=lambda kv: (kv[1], kv[0]), reverse=True))

    batsman = list(individual_runs.keys())[:10]
    runs = list(individual_runs.values())[:10]
    color = []

    for row in range(0, 10):
        if runs[row] <= 1000:
            color.append('red')
        elif 1000 < runs[row] < 2000:
            color.append('blue')
        else:
            color.append('green')

    # plotting bar graph
    left = list(range(1, 11))
    for a, b in zip(left, runs):
        plt.text(-0.25+a, 25+b, str(b))

    plt.bar(left, runs, tick_label=batsman, width=0.8, color=color)
    plt.xlabel('Batsman')
    plt.ylabel('Total Runs Scored')
    plt.title('Top RCB Batsman Run status')
    plt.show()


if __name__ == "__main__":
    plot()
