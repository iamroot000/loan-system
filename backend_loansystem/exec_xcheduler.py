import datetime
import time
from controller.xcheduler import DXcheduler

DX = DXcheduler()

def _update():
    print(DX.update())

while True:
    # Get the current time
    now = datetime.datetime.now()

    # Check if it's midnight
    if now.hour == 0 and now.minute == 0:
        _update()
    print('not yet')
    # Sleep for 60 seconds before checking again
    time.sleep(60)