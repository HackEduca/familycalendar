import sys
import locale

from funcs import echoMsg, echoError, _
from get_next_events import getNextEvents
from get_weather_data import getWeatherData
from generate_calendar import generateCalendar
from generate_weather import generateWeather
from generate_page import generatePage
from generate_page_error import generatePageError
from generate_image import generateImage

from settings import CUSTOM_LOCALE

locale.setlocale(locale.LC_ALL, CUSTOM_LOCALE)

def main():

    echoMsg(_('Start'))

    echoMsg(_('Getting calendar events'))
    if not getNextEvents():
        generatePageError(_('Cannot get calendar events'))
        exit(1)

    echoMsg(_('Getting weather forecast'))
    if not getWeatherData():
        generatePageError(_('Cannot get weather forecast'))
        exit(2)

    echoMsg(_('Generanting HTML from the events'))
    if not generateCalendar():
        exit(3)

    echoMsg(_('Generanting HTML from weather forecast'))
    if not generateWeather():
        exit(4)

    echoMsg(_('Generanting HTML page'))
    if not generatePage():
        exit(5)

    echoMsg(_('Generating JPG image from the HTML page'))
    if not generateImage():
        exit(6)

    echoMsg(_('Done!'))

if __name__ == '__main__':
    main()
