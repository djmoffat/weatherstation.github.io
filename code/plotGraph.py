#!/usr/bin/python3

import matplotlib.pyplot as plt
import datetime
import pandas as pd

def parseArgs(args):
    return None

def generateGraph(data_file='weather_data.csv',output_figure='images/weather.png'):
    data = pd.read_csv(data_file,parse_dates=True)
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

    plt.savefig(output_figure)

if __name__ == "__main__":
    generateGraph()
