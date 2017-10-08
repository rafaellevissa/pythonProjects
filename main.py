import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave

signalFromGPIO = 0;

if signalFromGPIO == 0:
    
    # Tenta realizar o cadastro do sinal na base de dados
	try:
		signalSave(signalFromGPIO)
	except Exception as e:
		print("Erro ao tentar cadastrar um Sinal: ", e)
