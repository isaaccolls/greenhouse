import time
import datetime
try:
    import RPi.GPIO as GPIO
    prod_env = True
except RuntimeError:
    prod_env = False

relay_grass = 14
relay_pine = 15
relay_lights = 2

if prod_env:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_grass, GPIO.OUT)
    GPIO.setup(relay_pine, GPIO.OUT)
    GPIO.setup(relay_lights, GPIO.OUT)


def relay_action(relay, action):
    print("relay: " + relay + ", action: " + action)
    # time.sleep(1)


# def relay_grass_on():
#     print("relay_grass_on 👍️")
#     if prod_env:
#         GPIO.output(relay_grass, True)
#         time.sleep(1)


# def relay_grass_off():
#     print("relay_grass_off 👎️")
#     if prod_env:
#         GPIO.output(relay_grass, False)
#         time.sleep(1)


# def fan_cooler_on():
#     print("fan_cooler_on")
#     if prod_env:
#         GPIO.output(relay_pine, True)
#         time.sleep(1)


# def fan_cooler_off():
#     print("fan_cooler_off")
#     if prod_env:
#         GPIO.output(relay_pine, False)
#         time.sleep(1)


# def status_blink():
#     print("blink status")
#     GPIO.output(status, True)


def do_it():
    print("do_it")
    relay_action(relay_grass, True)
    # datetime_object = datetime.datetime.now()
    # actual_hr = datetime_object.hour
    # actual_min = datetime_object.minute
    # print('datetime_object: {}'.format(datetime_object))
    # print('actual_hr: {}'.format(actual_hr))
    # print('actual_min: {}'.format(actual_min))
    # led_panel_on_hr = 6
    # led_panel_off_hr = 23
    # if actual_hr >= led_panel_on_hr and actual_hr < led_panel_off_hr:
    #     led_panel_on()
    # else:
    #     led_panel_off()
    # if (actual_min % 10 == 0):
    #     fan_cooler_on()
    # else:
    #     fan_cooler_off()


if __name__ == '__main__':
    do_it()
    print('this is the end')
