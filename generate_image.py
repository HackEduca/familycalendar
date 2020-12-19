import imgkit

def generateImage():

    options = {
        'format': 'jpg',
        'quiet': ''
        }

    imgkit.from_file('page/index.html', 'page/calendar.jpg', options=options)

    return True

if __name__ == '__main__':
    generateImage()
