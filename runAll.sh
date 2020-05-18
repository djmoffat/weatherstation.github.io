cd /home/pi/weatherstation.github.io
python3 code/getWeatherData.py >> weather_data.csv
python3 code/plotGraph.py
git commit -am "update"
git push
