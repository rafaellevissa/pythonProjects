import RPi.GPIO as GPIO #importa a biblioteca das GPIO
import time #biblioteca de tempo

PIN=16

def acao_detectada():
	print ("cadeado produzido")

GPIO.setmode(GPIO.BOARD) #configura o modo de definicao de pinos como BOARD
GPIO.setwarnings(False) #destiva avisos
GPIO.setup(PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #resistencia interna no input
GPIO.add_event_detect(PIN, GPIO.FALLING) #cadastrando evento de borda de descida
while (1):
    if(GPIO.event_detected(PIN)): #se detectar o evento cadastrado
        acao_detectada()
    time.sleep(.1) #aguarda 100 ms
    print(".")
    
