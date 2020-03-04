import csv
from datetime import datetime
from matplotlib import pyplot as plt  

filename = input("Enter the name of csv file: ")

dates, highs, lows = [], [], []
try:
    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                station_name = row[1]
                high = int(row[6])
                low = int(row[7])
    
            except ValueError:
                continue
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

except FileNotFoundError:
    print("There is no such file!")
    exit()
c_highs = [(value-32)/1.8 for value in highs]
c_lows = [(value-32)/1.8 for value in lows]

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, c_highs, c='purple')
plt.plot(dates, c_lows, c='blue')
plt.fill_between(dates, c_highs, c_lows, facecolor='blue', alpha=0.1)
title = "Lowest and highest temperature in " + station_name
plt.title(title, fontsize=24)
fig.autofmt_xdate()
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both',which='major', labelsize=16)
save_filename = input("Enter a name for your chart: ")
plt.savefig(save_filename, bbox_inches='tight')