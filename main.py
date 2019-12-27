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
    print("Off fan_cooler")
    if prod_env:
        GPIO.output(fan_cooler, False)
        time.sleep(1)


def status_blink():
    print("blink status")
    GPIO.output(status, True)


def do_it():
    print("do_it")
    datetime_object = datetime.datetime.now()
    print('datetime_object: {}'.format(datetime_object))
    actual_hour = datetime_object.hour
    print('actual_hour: {}'.format(actual_hour))
    actual_minute = datetime_object.minute
    print('actual_minute: {}'.format(actual_minute))
    led_panel_on_hour = 7
    led_panel_off_hour = 21
    if actual_hour > led_panel_on_hour and actual_hour < led_panel_off_hour:
        led_panel_on()
    else:
        led_panel_off()


if __name__ == '__main__':
    do_it()
    print('this is the end')
