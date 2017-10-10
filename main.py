import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
<<<<<<< HEAD
from sqliteQuerys import selectLineProduction
=======
>>>>>>> ac337cda66260511c2a6cf34076c8c206f6c2c2f

signalFromGPIO = 0;

if signalFromGPIO == 0:
    
    # Tenta realizar o cadastro do sinal na base de dados
	try:
<<<<<<< HEAD
		signalSave(signalFromGPIO, selectLineProduction())
=======
		signalSave(signalFromGPIO)
>>>>>>> ac337cda66260511c2a6cf34076c8c206f6c2c2f
	except Exception as e:
		print("Erro ao tentar cadastrar um Sinal: ", e)
