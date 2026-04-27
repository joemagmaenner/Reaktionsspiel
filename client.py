import requests
import json

SERVER_URL = 'http://localhost:8080'

def post_data(name_game, name_user, time):
    payload = {
        'name_game': name_game,
        'name_user': name_user,
        'time': time
    }
    response = requests.post(SERVER_URL, json=payload)
    if response.status_code == 201:
        print('Daten erfolgreich gesendet!')
    else:
        print('Fehler beim Senden:', response.json())

def get_data():
    response = requests.get(SERVER_URL)
    if response.status_code == 200:
        data = response.json()
        print('Gespeicherte Daten:')
        for entry in data:
            print(entry)
    else:
        print('Fehler beim Abrufen der Daten:', response.status_code)

if __name__ == '__main__':
    # Beispiel: POST-Daten senden
    post_data('SuperGame', 'Alice', 120)
    post_data('MegaGame', 'Bob', 95)

    # Beispiel: GET-Daten abrufen
    get_data()