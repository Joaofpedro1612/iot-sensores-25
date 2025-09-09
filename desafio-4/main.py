from machine import Pin, time_pulse_us
import time

TRIG_PIN = 12
ECHO_PIN = 14
LED_ALERTA = 25
LED_SUCESSO = 26

trig_pin = Pin(TRIG_PIN, Pin.OUT)
echo_pin = Pin(ECHO_PIN, Pin.IN)
led_alerta = Pin(LED_ALERTA, Pin.OUT)
led_sucesso = Pin(LED_SUCESSO, Pin.OUT)

def medir_distancia():
    trig_pin.value(0)
    time.sleep_us(2)

    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)

    duracao = time_pulse_us(echo_pin, 1, 30000)
    distancia = (duracao / 2) * 0.0343  
    return distancia


contador_objetos = 0
objeto_presente = False  

while True:
    distancia = medir_distancia()
    print("Distância:", distancia, "cm")

    if distancia <= 7:  
        led_alerta.value(1)

        if not objeto_presente:
            contador_objetos += 1
            objeto_presente = True
            print("Novo objeto detectado! Contagem:", contador_objetos)

            led_alerta.value(0)
            time.sleep(0.1)
            led_alerta.value(1)

            if contador_objetos >= 5:
                print("Meta atingida! Acendendo LED verde...")
                led_sucesso.value(1)
                time.sleep(5)  
                led_sucesso.value(0)
                contador_objetos = 0  
    else:
        led_alerta.value(0)
        objeto_presente = False  

    time.sleep(0.2)
