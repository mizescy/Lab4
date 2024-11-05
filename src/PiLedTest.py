import RPi.GPIO as GPIO
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

def main():
    switch.init()
    led.init()
    while True:

        if switch.read_slide_switch():
            led.set_output(0,1)
            sleep(0.1)
            led.set_output(0,0)
            sleep(0.1)
        else:
            led.set_output(0,1)
            sleep(0.05)
            led.set_output(0,0)
            sleep(0.05)

if __name__ == "__main__":
    main()