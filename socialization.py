import os
import random
import datetime
from time import sleep

from win10toast import ToastNotifier

FRIDAY = 4

def get_next_friday():
    friday = datetime.datetime.now()
    friday += datetime.timedelta(days=1)
    while friday.weekday() != FRIDAY:
        friday += datetime.timedelta(days=1)
    friday = friday.replace(hour=16, minute=0)
    return friday

next_friday = get_next_friday()
while True:
    if datetime.datetime.now() >= next_friday:
        next_friday = get_next_friday()

        friends = []
        with open('friends.txt', 'r') as file:
            for line in file:
                friends.append(line.strip())

        current = []
        with open('current.txt', 'r') as file:
            for line in file:
                current.append(line.strip())

        diff = [item for item in friends if item not in current]

        if not diff:
            os.remove('current.txt')
            diff = friends

        friend = random.choice(diff)

        icon = None
        if os.path.exists('./resources/socialization.ico'):
            icon = './resources/socialization.ico'

        toaster = ToastNotifier()
        toaster.show_toast(title='Socialize!',
                           msg='Talk to {}!'.format(friend),
                           duration=3600,
                           icon_path=icon)

        with open('current.txt', 'a') as file:
            file.write('{}\n'.format(friend))
    else:
        sleep(600)  # Sleep for 10 minutes