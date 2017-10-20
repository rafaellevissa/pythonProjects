import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import selectLineProduction
from sqliteQuerys import existSignalFromHour
from sqliteQuerys import signalUpdate
from sqliteQuerys import showMeTheProducaoTable
from sqliteQuerys import existLineProduction
from terminalClear import terminalClear
import datetime
import time

import RPi.GPIO as GPIO 

PIN = 16

# Configura o modo de definicao de pinos como BOARD
GPIO.setmode(GPIO.BOARD)

# Destiva avisos
GPIO.setwarnings(False) 

# Resistencia interna no input
GPIO.setup(PIN,GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 

# Cadastrando evento de borda de descida
GPIO.add_event_detect(PIN, GPIO.FALLING)



#-------------------------------------------------------------------------------
# Verifica se existe algum registro na Tabela Linha de Produção
#-------------------------------------------------------------------------------
if existLineProduction() == False:
	terminalClear()
	print("Voce esqueceu de Cadastrar uma Linha de Producao. \n Digite: python lineProduction.py para criar!")
	exit()
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Verifica se existe algum registro por hora atual e data atual
#-------------------------------------------------------------------------------
while (1):

	if GPIO.event_detected(PIN):

		if (existSignalFromHour() != True):

			try:

				signalSave(selectLineProduction())
				print("Novo registro realizado com Sucesso.")

				showMeTheProducaoTable()

			except Exception as e:
				print("Erro ao tentar Cadastrar um novo Registro: ", e)

		else:

			try:

				signalUpdate()
				print("Novo incremento realizado com Sucesso.")
				
				showMeTheProducaoTable()

			except Exception as e:
				print("Erro ao tentar Incrementar um Registro: ", e)
#-------------------------------------------------------------------------------