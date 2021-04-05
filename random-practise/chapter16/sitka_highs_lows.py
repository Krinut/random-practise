import csv	#imporitng csv module to parse through csv files
import matplotlib.pyplot as plt
from datetime import datetime	#this is used to convert the date string to date format

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
	reader = csv.reader(f)	#reading teh csv file and passing it into the reader object
	header_row = next(reader)	#nex() returns the next line in the file which is the header file

	#extracting data from the csv files and appending it into our lists
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		low = int(row[6])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)	#fill the gap in middle with blue hue color

plt.title("Daily high and low temperature-2018", fontsize=24)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
