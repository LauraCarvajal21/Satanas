import RPi.GPIO as GPIO
import time
import LCDLIB16x2 as LCD

# Initialise display
LCD.lcd_init()

while True:

    # Send some test
    LCD.lcd_string(" Rasbperry Pi ", LCD.LINE_1)
    LCD.lcd_string(" Hola bebe ", LCD.LINE_2)

    time.sleep(3)  # 3 second delay

    # Send some text
    LCD.lcd_string("PWM", LCD.LINE_1)
    LCD.lcd_string("#VUELTAS", LCD.LINE_2)

    time.sleep(3)  # 3 second delay

GPIO.cleanup()
