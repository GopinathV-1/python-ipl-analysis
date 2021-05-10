import csv
import matplotlib.pyplot as plt
umpire = []
# converting csv file to list
with open('umpires.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        umpire.append(row)
foreign_umpire = {}
# counting umpires based on origin of country
for row in range(1, len(umpire)):
    if foreign_umpire.get(umpire[row][0]) is None:
        foreign_umpire[umpire[row][0]] = umpire[row][1].strip()
umpire_count = {}
for row in foreign_umpire.items():
    cou = row[1]
    if cou == 'India':
        continue
    if umpire_count.get(cou) is None:
        umpire_count[cou] = 1
    else:
        umpire_count[cou] += 1
ump_country = []
ump_count = []
for row in umpire_count.items():
    ump_country.append(row[0])
    ump_count.append(row[1])
left = range(1, len(ump_count)+1)
color = []
for row in range(len(ump_country)):
    if ump_count[row] <= 2:
        color.append('red')
    elif ump_count[row] > 2 and ump_count[row] < 5:
        color.append('blue')
    else:
        color.append('green')
# plotting bar graph
plt.bar(left, ump_count, tick_label=ump_country, width=0.8, color=color)
plt.xlabel('Country')
plt.ylabel('Umpire\'s count')
plt.title('Foreign Umpire Analysis')
plt.show()
