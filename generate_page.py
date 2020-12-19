import pathlib
import locale
from datetime import datetime
from settings import CUSTOM_LOCALE
from funcs import _

def generatePage():

    # Get the last date and time data file modification
    eventsFile = pathlib.Path('data/events.json')
    assert eventsFile.exists(), f'No such file: {eventsFile}'

    lastUpdate = datetime.fromtimestamp(eventsFile.stat().st_mtime)

    with open('page/templates/main.html', 'r') as file:
        templateHTML = file.read()
        file.close()

    with open('out/calendar.html', 'r') as file:
        calendarHTML = file.read()
        file.close()

    with open('out/weather.html', 'r') as file:
        weatherHTML = file.read()
        file.close()

    # Due that strftime('%B') on some languages, for exemple on "ca_ES",
    # not returns only the month name but a prefix,
    # and I don't know how to adjust that issue,
    # I've to use that dict to get the right month names.
    MONTH_NAMES = {
                        1: _('January'),
                        2: _('February'),
                        3: _('March'),
                        4: _('April'),
                        5: _('May'),
                        6: _('June'),
                        7: _('July'),
                        8: _('August'),
                        9: _('September'),
                        10: _('October'),
                        11: _('November'),
                        12: _('December'),
                    }

    replaceStrings = {
                        'HTML_LANG': locale.getlocale()[0],
                        'PAGE_TITLE': _('Family calendar'),
                        'MONTH_NAME': MONTH_NAMES[lastUpdate.month],
                        'YEAR': str(lastUpdate.year),
                        'WEATHER': weatherHTML,
                        'CALENDAR': calendarHTML,
                        'LAST_UPDATE_LEGEND': _('Last update'),
                        'LAST_UPDATE': lastUpdate.strftime('%x %X')
                    }

    html = templateHTML
    for key, value in replaceStrings.items():
        html = html.replace(f'[[{key}]]', value)

    with open('page/index.html', 'wt') as fout:
        fout.write(html)
        fout.close()

    return True

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, CUSTOM_LOCALE)
    generatePage()
