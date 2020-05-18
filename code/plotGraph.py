#!/usr/bin/python

import matplotlib.pyplot as plt
import datetime
import pandas as pd

data = pd.read_csv('weather_data.csv',parse_dates=True)
ax = data.plot()
ax.legend(["Temperature (c)", "Humidity (%)"]);
fig = ax.get_figure()
plt.savefig('images/weather.png')
