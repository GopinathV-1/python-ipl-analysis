import csv
import matplotlib.pyplot as plt
total_runs = {}
deliveries = []
# converting csv files to list
with open('deliveries.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        deliveries.append(row)
individual_runs = {}
# calculating runs scored by rcb batsman
for row in range(1, len(deliveries)):
    if deliveries[row][2] == 'Royal Challengers Bangalore':
        if individual_runs.get(deliveries[row][6]) is None:
            individual_runs[deliveries[row][6]] = int(deliveries[row][17])
        else:
            individual_runs[deliveries[row][6]] += int(deliveries[row][17])
batsman = []
runs = []
individual_runs = dict(sorted(individual_runs.items(),
                              key=lambda kv: (kv[1], kv[0]), reverse=True))
for row in individual_runs.items():
    batsman.append(row[0])
    runs.append(row[1])
left = range(1, 11)
color = []
runs = runs[:10]
batsman = batsman[:10]
for row in range(0, 10):
    if runs[row] <= 1000:
        color.append('red')
    elif runs[row] > 1000 and runs[row] < 2000:
        color.append('blue')
    else:
        color.append('green')
# plotting bar graph
plt.bar(left, runs, tick_label=batsman, width=0.8, color=color)
plt.xlabel('Batsman')
plt.ylabel('Total Runs Scored')
plt.title('Top RCB Batsman Run status')
plt.show()
