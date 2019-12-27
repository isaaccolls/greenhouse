import time
import datetime
try:
    import RPi.GPIO as GPIO
    prod_env = True
except RuntimeError:
    prod_env = False

led_panel = 20
fan_cooler = 16
status = 21

if prod_env:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_panel, GPIO.OUT)
    GPIO.setup(fan_cooler, GPIO.OUT)
    GPIO.setup(status, GPIO.OUT)


def led_panel_on():
    print("led_panel_on")
    if prod_env:
        GPIO.output(led_panel, True)
        time.sleep(1)


def led_panel_off():
    print("led_panel_off")
    if prod_env:
        GPIO.output(led_panel, False)
        time.sleep(1)


def fan_cooler_on():
    print("fan_cooler_on")
    if prod_env:
        GPIO.output(fan_cooler, True)
        time.sleep(1)


def fan_cooler_off():
    print("fan_cooler_off")
    if prod_env:
        GPIO.output(fan_cooler, False)
        time.sleep(1)


def status_blink():
    print("blink status")
    GPIO.output(status, True)


def do_it():
    print("do_it")
    datetime_object = datetime.datetime.now()
    actual_hr = datetime_object.hour
    actual_min = datetime_object.minute
    print('datetime_object: {}'.format(datetime_object))
    print('actual_hr: {}'.format(actual_hr))
    print('actual_min: {}'.format(actual_min))
    led_panel_on_hr = 7
    led_panel_off_hr = 21
    if actual_hr >= led_panel_on_hr and actual_hr < led_panel_off_hr:
        led_panel_on()
    else:
        led_panel_off()
    fan_cooler_on_min = 0
    fan_cooler_off_min = 15
    if actual_min >= fan_cooler_on_min and actual_min < fan_cooler_off_min:
        fan_cooler_on()
    else:
        fan_cooler_off()


if __name__ == '__main__':
    do_it()
    print('this is the end')
