import json
from datetime import datetime, date, timedelta
from settings import CALENDAR_LIST

def generateCalendar():

    # Load the events file obtained by getNextEvents
    events = json.load(open('data/events.json'))

    # Current date and time
    currentDate = date.today()
    currentTime = datetime.now()

    # Get the first month date
    calendarDate = currentDate.replace(day=1)

    # If first month date is not monday,
    # we go back to find the monday
    while calendarDate.weekday() != 0:
        calendarDate = (calendarDate - timedelta(days=1))

    html = ''

    # 6 weeks height
    for row in range(6):

        html += '<div class="calendar-row">'

        # 7 days wide
        for col in range(7):

            classCol = ' another-month' if calendarDate.month != currentDate.month else ''
            classCol += ' current-date' if calendarDate == currentDate else ''
            classCol += ' pass-day' if calendarDate < currentDate else ''
            classCol += ' weekend-day' if calendarDate.weekday() == 5 or calendarDate.weekday() == 6 else ''

            html += '<div class="calendar-col' + classCol + '">'
            html +=     '<div class="calendar-day"><span class="calendar-day-number">' + str(calendarDate.day) + '</span></div>'
            html +=     '<div class="calendar-events-day">'

            dayEvents = list(filter(lambda d: d['start'][0:10] >= calendarDate.isoformat() and d['start'][0:10] <= calendarDate.isoformat(), events))
            for event in dayEvents:

                # The 'start' has the format "yyyy-mm-ddThh:MM:SS+01:00"
                eventTime = datetime.strptime(event['start'], '%Y-%m-%dT%H:%M:%S+01:00')

                eventClass = ' pass-time' if eventTime < currentTime else ''

                html += '<div class="calendar-event' + eventClass + '">'
                html +=     '<span class="calendar-time">' + eventTime.strftime('%H:%M') + '</span>'
                html +=     '<span class="calendar-owner">' + CALENDAR_LIST[event['owner']] + '</span>'
                html +=     '<span class="calendar-summary">' + event['summary'] + '</span>'
                html += '</div>' # calendar-event

            html += '</div>' # calendar-events-day

            calendarDate = (calendarDate + timedelta(days=1))
            html += '</div>' # calendar-col

        html += '</div>' # calendar-row

    # Save the html
    # The generatePage will compose the final page
    with open('out/calendar.html', 'wt') as fout:
        fout.write(html)
        fout.close()

    return True

if __name__ == '__main__':
    generateCalendar()
