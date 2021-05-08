import csv
import matplotlib.pyplot as plt


# making abbreviation names
def short(name):
    split_name = name.split(' ')
    short_name = [each[0] for each in split_name]
    return ''.join(short_name)


total_runs = {}
deliveries = []
# converting csv file to list
with open('deliveries.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        deliveries.append(row)
# calculating total runs by each team
for row in range(1, len(deliveries)):
    if total_runs.get(deliveries[row][2]) is None:
        total_runs[deliveries[row][2]] = int(deliveries[row][17])
    else:
        total_runs[deliveries[row][2]] += int(deliveries[row][17])
team = []
team_full = {}
run = []
team_name = {}
team_matching = {}
for row in total_runs.items():
    name = short(row[0])
    team_full[name] = row[0]
    if team_matching.get(name) is None:
        team_matching[name] = row[1]
    else:
        team_matching[name] += row[1]
for row in team_matching.items():
    team.append(row[0])
    run.append(row[1])
color = []
for col in run:
    if col <= 10000:
        color.append('red')
    elif col > 10000 and col < 20000:
        color.append('blue')
    else:
        color.append('green')
left = range(1, len(team)+1)
# plotting bar graph
plt.bar(left, run, tick_label=team, width=0.8, color=color)
plt.xlabel('Team')
plt.ylabel('Total Runs Scored')
plt.title('Run status')
plt.show()
