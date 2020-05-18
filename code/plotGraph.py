#!/usr/bin/python3

import matplotlib.pyplot as plt
import datetime
import pandas as pd

data = pd.read_csv('weather_data.csv',parse_dates=True)
x = pd.to_datetime(data['date-time'])
t = data['temperature']
h = data['humidity']
plt.xlabel('Real-Time') 
plt.ylabel('Value') 
plt.title('Title')
plt.plot(x, t)
plt.plot(x, h)
plt.legend(["Temperature (c)", "Humidity (%)"]);

plt.gcf().autofmt_xdate()
plt.show()

plt.savefig('images/weather.png')
