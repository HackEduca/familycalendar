import json
from datetime import datetime, date, timedelta
from settings import WEATHER_ICONS, UNITS_SYSTEM

def generateWeather():

    # Carreguem el fitxer events.json que haurà generat nextevents.py
    weatherData = json.load(open('data/weather.json'))

    tempMeasure = 'C' if UNITS_SYSTEM == 'metric' else 'F'

    maxDays = 5
    html = ''
    for fc in weatherData:

        weatherDate = datetime.fromtimestamp(fc['date'])

        # Si el códi de la condició del temps no existeix en WEATHER_ICONS
        # Fiquem el códi 999
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

    # Ho guardem en weather.html
    # Altre procés s'encarrega de ficar-ho on cal
    with open('out/weather.html', 'wt') as fout:
        fout.write(html)
        fout.close()

    return True

if __name__ == '__main__':
    generateWeather()