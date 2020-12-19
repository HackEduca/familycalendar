import json
from datetime import datetime, date, timedelta
from settings import WEATHER_ICONS, UNITS_SYSTEM

def generateWeather():

    # Load the JSON weather data collected by getWeatherData
    weatherData = json.load(open('data/weather.json'))

    tempMeasure = 'C' if UNITS_SYSTEM == 'metric' else 'F'

    maxDays = 5
    html = ''
    for fc in weatherData:

        weatherDate = datetime.fromtimestamp(fc['date'])

        # If the weather condition code not exists in WEATHER_ICONS
        # use the 999 code to tell that something was wrong
        icon = WEATHER_ICONS[fc['weather_code']] if fc['weather_code'] in WEATHER_ICONS else WEATHER_ICONS[999]

        html += '<div class="weather-col">'
        html +=     '<div class="weather-row">'
        html +=         '<div class="weather-day">' + str(weatherDate.day) + '</div>'
        html +=         '<div class="weather-img"><img src="' + icon + '" width="32" height="auto"></div>'
        html +=     '</div>'
        html +=     '<div class="weather-row">'
        html +=         '<div class="weather-temp">&uarr;' + str(int(round(fc['tempMax']))) + 'º' + tempMeasure + ' &darr;' + str(int(round(fc['tempMin']))) + 'º' + tempMeasure + '</div>'
        html +=     '</div>'
        html += '</div>'

        maxDays -= 1

        if maxDays == 0:
            break

    # Save the html
    # The generatePage will compose the final page
    with open('out/weather.html', 'wt') as fout:
        fout.write(html)
        fout.close()

    return True

if __name__ == '__main__':
    generateWeather()