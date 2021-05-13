import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def plot():
    '''Plotting bar graph for top
       run scored RCB batsman'''

    # creating dictionary of RCB batsman and their scores
    rcb_batsman_runs = defaultdict(int)
    with open('deliveries.csv', 'r') as file:
        deliveries = csv.DictReader(file)
        for row in deliveries:
            if row['batting_team'] == 'Royal Challengers Bangalore':
                rcb_batsman_runs[row['batsman']] += int(row['total_runs'])

    # Descending sort of batsman based on their scores
    rcb_batsman_runs = dict(sorted(rcb_batsman_runs.items(),
                            key=lambda kv: (kv[1], kv[0]), reverse=True))

    top_batsman_name = list(rcb_batsman_runs.keys())[:10]
    top_runs_scored = list(rcb_batsman_runs.values())[:10]
    color = []

    for row in top_runs_scored:
        if row <= 1000:
            color.append('red')
        elif 1000 < row < 2000:
            color.append('blue')
        else:
            color.append('green')

    # plotting bar graph
    graph_length = list(range(1, len(top_batsman_name)+1))
    for a, b in zip(graph_length, top_runs_scored):
        plt.text(-0.25+a, 25+b, str(b))

    plt.bar(graph_length, top_runs_scored, tick_label=top_batsman_name,
            width=0.8, color=color)
    plt.xlabel('Batsman')
    plt.ylabel('Total Runs Scored')
    plt.title('Top RCB Batsman Run status')
    plt.show()


if __name__ == "__main__":
    plot()
