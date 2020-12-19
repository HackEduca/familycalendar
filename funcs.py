import sys
import gettext
import locale

from datetime import datetime

def echoMsg(msg):
    _echoMsg(msg, sys.stdout)

def echoError(msg):
    errorTXT = _('ERROR')
    _echoMsg(f'[{errorTXT}] {msg}\n', sys.stderr)

def _echoMsg(msg, fileOut):
    currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fileOut.write(f'[{currentTime}] {msg}\n')

def _(txt):

    currentLang = locale.getlocale()[0]

    # The original texts are in english
    if currentLang == 'en_GB' or currentLang == 'en_US' or currentLang == 'en':
        return txt

    trans = gettext.translation('familycalendar', './locale', languages=(currentLang,))
    return trans.gettext(txt)
