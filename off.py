import RPi.GPIO as GPIO
import time

led_panel = 14
fan_cooler = 15
status = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_panel, GPIO.OUT)
GPIO.setup(fan_cooler, GPIO.OUT)
GPIO.setup(status, GPIO.OUT)


def off_everything():
    print("off led_panel")
    GPIO.output(led_panel, False)
    print("off fan_cooler")
    GPIO.output(fan_cooler, False)
    print("off status")
    GPIO.output(status, False)
    time.sleep(1)
    print("bye")


if __name__ == '__main__':
    off_everything()
