import pathlib
import locale
from datetime import datetime
from settings import CUSTOM_LOCALE
from funcs import _

def generatePageError(errorMsg):

    lastUpdate = datetime.now()

    with open('page/templates/error.html', 'r') as file:
        templateHTML = file.read()
        file.close()

    replaceStrings = {
                        'HTML_LANG': locale.getlocale()[0],
                        'PAGE_TITLE': _('Family calendar'),
                        'ERROR_MESSAGE': errorMsg,
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
    generatePageError('ERROR TEST')
