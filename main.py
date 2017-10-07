import sqlite3
from dataBaseName import dataBaseName
from signalSave import signalSave

signalFromGPIO = 0;

if signalFromGPIO == 0:

	try:
		signalSave(signalFromGPIO)
	except Exception as e:
		print("Erro ao tentar cadastrar um Sinal: ", e)