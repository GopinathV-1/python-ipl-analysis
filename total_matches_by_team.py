import csv
import matplotlib.pyplot as plt


# referencing a team to another as both belongs to same
def team_name(name):
    if name == 'Rising Pune Supergiants':
        return "Rising Pune Supergiant"
    return name


matches = []
# converting csv files to list
with open('matches.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        matches.append(row)
teams = {}
# calculating total matches in a season by a team
for row in range(1, len(matches)):
    t1 = team_name(matches[row][4])
    t2 = team_name(matches[row][5])
    teams[t1] = {}
    teams[t2] = {}
for row in teams.keys():
    for col in range(2008, 2018):
        teams[row][str(col)] = 0
for row in range(1, len(matches)):
    year = matches[row][1]
    t1 = team_name(matches[row][4])
    t2 = team_name(matches[row][5])
    teams[t1][year] += 1
    teams[t2][year] += 1
left = []
for row in range(2008, 2018):
    left.append(row)
s_m = []
team = []
for row in teams.items():
    t = []
    team.append(row[0])
    for col in row[1].items():
        t.append(col[1])
    s_m.append(t)
b_m = []
for row in range(0, len(s_m)):
    L = []
    for col in range(0, len(s_m[row])):
        if row == 0:
            L.append(s_m[row][col])
        else:
            L.append(b_m[row-1][col]+s_m[row][col])
    b_m.append(L)
# plotting stacked bar graph
plt.bar(left, s_m[0], 0.4, tick_label=left, color='orange', label='SH')
plt.bar(left, s_m[1], 0.4, bottom=b_m[0], color='red', label='RCB')
plt.bar(left, s_m[2], 0.4, bottom=b_m[1], color='blue', label='MI')
plt.bar(left, s_m[3], 0.4, bottom=b_m[2], color='pink', label='RPS')
plt.bar(left, s_m[4], 0.4, bottom=b_m[3], color='darkblue', label='GL')
plt.bar(left, s_m[5], 0.4, bottom=b_m[4], color='purple', label='KKR')
plt.bar(left, s_m[6], 0.4, bottom=b_m[5], color='black', label='KXP')
plt.bar(left, s_m[7], 0.4, bottom=b_m[6], color='green', label='DD')
plt.bar(left, s_m[8], 0.4, bottom=b_m[7], color='yellow', label='CSK')
plt.bar(left, s_m[9], 0.4, bottom=b_m[8], color='cyan', label='RR')
plt.bar(left, s_m[10], 0.4, bottom=b_m[9], color='gray', label='DC')
plt.bar(left, s_m[11], 0.4, bottom=b_m[10], color='peru', label='KTK')
plt.bar(left, s_m[12], 0.4, bottom=b_m[11], color='royalblue', label='PW')
plt.xlabel('Season')
plt.ylabel('Matches Played by Team')
plt.legend()
plt.title('Matches Played by Team by Season')
plt.show()
