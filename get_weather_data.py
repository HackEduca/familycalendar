import sys
import json

from datetime import datetime

# From: https://github.com/csparpa/pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from funcs import echoMsg, echoError
from settings import OWM_API_KEY, UNITS_SYSTEM

def getWeatherData():

    try:

        owm = OWM(OWM_API_KEY)
        mgr = owm.weather_manager()
        one_call = mgr.one_call(lat=39.46975, lon=-0.37739, units=UNITS_SYSTEM)

        weatherForecast = []

        currentDate = datetime.now()

        for fc in one_call.forecast_daily:

            # Descartem dates passades
            if datetime.fromtimestamp(fc.ref_time) < currentDate:
                continue

            dayFC = {
                        'date': fc.ref_time,
                        'weather_code': fc.weather_code,
                        'tempMin': fc.temperature().get('min'),
                        'tempMax': fc.temperature().get('max')
                    }

            weatherForecast.append(dayFC)

        with open('data/weather.json', 'w') as fout:
            json.dump(weatherForecast, fout)

        return True

    except:
        e = sys.exc_info()[1]
        echoError(str(e))
        return False

if __name__ == '__main__':
    getWeatherData()
