import os
import ast
from dotenv import load_dotenv

# Set the data in a .env file
# You can see the env-example file
load_dotenv()

# The language for texts
# en_US.UTF8, en_GB.UTF8, es_ES.UTF8
# Look at locale/ dir to see the available translations
# You can add your own translation
# If leave empty, the system local will be used
CUSTOM_LOCALE = os.getenv('CUSTOM_LOCALE')

# Can get it on https://home.openweathermap.org/api_keys
OWM_API_KEY = os.getenv('OWM_API_KEY')

# Your latitude and longitude coordinates in degrees
# You can get it from https://www.latlong.net/
OWN_LATITUDE = float(os.getenv('OWM_LATITUDE'))
OWN_LONGITUDE = float(os.getenv('OWM_LONGITUDE'))

# 'metric' or 'imperial'
UNITS_SYSTEM = os.getenv('UNITS_SYSTEM')

# CALENDAR_LIST = "{'yourmail@gmail.com':'Y','groupcalendarID@group.calendar.google.com':'G','sonsmail@gmail.com':'S'}"
CALENDAR_LIST = ast.literal_eval(os.getenv('CALENDAR_LIST'))

# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
WEATHER_ICONS = {

                    200: 'img/weather-icons/wi-day-storm-showers.svg', # thunderstorm with light rain
                    201: 'img/weather-icons/wi-day-storm-showers.svg', # thunderstorm with rain
                    202: 'img/weather-icons/wi-day-storm-showers.svg', # thunderstorm with heavy rain
                    210: 'img/weather-icons/wi-day-lightning.svg', # light thunderstorm
                    211: 'img/weather-icons/wi-day-thunderstorm.svg', # thunderstorm
                    212: 'img/weather-icons/wi-lightning.svg', # heavy thunderstorm
                    221: 'img/weather-icons/wi-lightning.svg', # ragged thunderstorm
                    230: 'img/weather-icons/wi-day-sleet-storm.svg', # thunderstorm with light drizzle
                    231: 'img/weather-icons/wi-day-sleet-storm.svg', # thunderstorm with drizzle
                    232: 'img/weather-icons/wi-day-sleet-storm.svg', # thunderstorm with heavy drizzle

                    300: 'img/weather-icons/wi-day-sprinkle.svg', # light intensity drizzle
                    301: 'img/weather-icons/wi-day-rain-mix.svg', # drizzle
                    302: 'img/weather-icons/wi-day-rain-mix.svg', # heavy intensity drizzle
                    310: 'img/weather-icons/wi-rain-mix.svg', # light intensity drizzle rain
                    311: 'img/weather-icons/wi-rain-mix.svg', # drizzle rain
                    312: 'img/weather-icons/wi-rain-mix.svg', # heavy intensity drizzle rain
                    313: 'img/weather-icons/wi-showers.svg', # shower rain and drizzle
                    314: 'img/weather-icons/wi-showers.svg', # heavy shower rain and drizzle
                    321: 'img/weather-icons/wi-showers.svg', # shower drizzle

                    500: 'img/weather-icons/wi-day-rain.svg', # light rain
                    501: 'img/weather-icons/wi-day-rain.svg', # moderate rain
                    502: 'img/weather-icons/wi-rain.svg', # heavy intensity rain
                    503: 'img/weather-icons/wi-sprinkle.svg', # very heavy rain
                    504: 'img/weather-icons/wi-sprinkle.svg', # extreme rain
                    511: 'img/weather-icons/wi-rain.svg', # freezing rain
                    520: 'img/weather-icons/wi-rain.svg', # light intensity shower rain
                    521: 'img/weather-icons/wi-rain.svg', # shower rain
                    522: 'img/weather-icons/wi-rain.svg', # heavy intensity shower rain
                    531: 'img/weather-icons/wi-rain.svg', # ragged shower rain

                    600: 'img/weather-icons/wi-day-snow.svg', # light snow
                    601: 'img/weather-icons/wi-snow.svg', # snow
                    602: 'img/weather-icons/wi-snowflake-cold.svg', # heavy snow
                    611: 'img/weather-icons/wi-sleet.svg', # sleet
                    612: 'img/weather-icons/wi-sleet.svg', # light shower sleet
                    613: 'img/weather-icons/wi-sleet.svg', # shower sleet
                    615: 'img/weather-icons/wi-day-snow-wind.svg', # light rain and snow
                    616: 'img/weather-icons/wi-day-snow-wind.svg', # rain and snow
                    620: 'img/weather-icons/wi-day-snow-wind.svg', # light shower snow
                    621: 'img/weather-icons/wi-day-snow-wind.svg', # shower snow
                    622: 'img/weather-icons/wi-snowflake-cold.svg', # heavy shower snow

                    700: 'img/weather-icons/wi-dust.svg', # mist
                    711: 'img/weather-icons/wi-smog.svg', # smoke
                    721: 'img/weather-icons/wi-day-haze.svg', # haze
                    731: 'img/weather-icons/wi-sandstorm.svg', # sand / dust
                    741: 'img/weather-icons/wi-fog.svg', # fog
                    751: 'img/weather-icons/wi-sandstorm.svg', # sand
                    761: 'img/weather-icons/wi-dust.svg', # dust
                    762: 'img/weather-icons/wi-volcano.svg', # volcanic ash
                    771: 'img/weather-icons/wi-cloudy-gusts.svg', # squalls
                    781: 'img/weather-icons/wi-tornado.svg', # tornado

                    800: 'img/weather-icons/wi-day-sunny.svg', # clear
                    801: 'img/weather-icons/wi-day-cloudy.svg', # few clouds with sun
                    802: 'img/weather-icons/wi-day-cloudy-high.svg', # scattered clouds (light clouds)
                    803: 'img/weather-icons/wi-cloud.svg', # broken clouds (mostly cloud)
                    804: 'img/weather-icons/wi-cloudy.svg', # overcast clouds (all covered by clouds)

                    999: 'img/weather-icons/wi-alien.svg' # Unknown weather code

                }


