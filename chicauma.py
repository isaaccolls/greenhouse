import time
import datetime
try:
    import RPi.GPIO as GPIO
    prod_env = True
except RuntimeError:
    prod_env = False

# relay pinout
relay_grass = 15
relay_pine = 14
relay_light = 2

if prod_env:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_grass, GPIO.OUT)
    GPIO.setup(relay_pine, GPIO.OUT)
    GPIO.setup(relay_light, GPIO.OUT)


def relay_action(relay, action):
    print("relay: " + str(relay) + ", action: " + str(action))
    if prod_env:
        GPIO.output(relay, action)
        time.sleep(1)


def check_grass(weekday, hour, minute):
    print('-- check_grass')
    if hour == 9 and (minute >= 0 and minute <= 15):
        relay_action(relay_grass, False)
    else:
        relay_action(relay_grass, True)


def check_pine(weekday, hour, minute):
    print('-- check_pine')
    if (weekday == 0 or weekday == 2 or weekday == 4) and hour == 7 and (minute >= 0 and minute <= 25):
        relay_action(relay_pine, False)
    else:
        relay_action(relay_pine, True)


def check_light(hour):
    print('-- check_light')
    if hour >= 21 or hour <= 4:
        relay_action(relay_light, False)
    else:
        relay_action(relay_light, True)


def do_it():
    print("do_it")
    datetime_object = datetime.datetime.now()
    print("datetime_object: {}".format(datetime_object))
    weekday = datetime_object.weekday()
    hour = datetime_object.hour
    minute = datetime_object.minute
    print('weekday: {}, hour: {}, minute: {}'.format(weekday, hour, minute))
    check_grass(weekday, hour, minute)
    check_pine(weekday, hour, minute)
    check_light(hour)


if __name__ == '__main__':
    do_it()
    print('🔥')
