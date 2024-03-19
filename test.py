from playsound import playsound
import requests


def synthesize(text):
    url = "https://api.chimege.com/v1.2/synthesize"
    headers = {
        'Content-Type': 'plain/text',
        'Token': '3a05b3a614188441623e778b4475e7f59e0a2f1552314168f51d0d8fb0c3356e',
    }

    r = requests.post(
        url, data=text.encode('utf-8'), headers=headers)

    with open("audio.wav", 'wb') as out:
        out.write(r.content)


print(synthesize('Сайн бай'))

playsound('audio.wav')