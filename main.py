import RPi.GPIO as GPIO
import time
import LCDLIB16X2 as LCD

# Initialise display
BOTON_SUBIR = 14
BOTON_BAJAR = 4

LCD.lcd_init()
GPIO.setmode(GPIO.BCM)
GPIO.setup(BOTON_SUBIR, GPIO.IN)
GPIO.setup(BOTON_BAJAR, GPIO.IN)


def main():
    corriendo = True
    velodicad = 0
    sentido = 0
    vueltas = 0

    bandera_posicion = 0

    while corriendo:
        subir = GPIO.input(BOTON_SUBIR)
        bajar = GPIO.input(BOTON_BAJAR)

        if subir == True and bandera_posicion<=2:
            bandera_posicion+=1
        elif bajar == True and bandera_posicion>=0:
            bandera_posicion-=1
        # Mi menu
        if bandera_posicion == 0:
            LCD.lcd_string("Velocidad      *", LCD.LINE_1)
            LCD.lcd_string("Sentido", LCD.LINE_2)
        elif bandera_posicion == 1:
            LCD.lcd_string("Velocidad ", LCD.LINE_1)
            LCD.lcd_string("Sentido        *", LCD.LINE_2)
        elif bandera_posicion == 2:
            LCD.lcd_string("Sentido", LCD.LINE_1)
            LCD.lcd_string("Vueltas        *", LCD.LINE_2)

    GPIO.cleanup()


main()
