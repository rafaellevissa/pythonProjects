import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import selectLineProduction
from sqliteQuerys import existSignalFromHora
from sqliteQuerys import signalUpdate
import datetime

signalFromGPIO = 0;

time = datetime.datetime.now()


if (existSignalFromHora(time.hour) != True):

	try:
		signalSave(time.hour, selectLineProduction())
		print("Novo registro realizado com Sucesso.")
	except Exception as e:
		print("Erro ao tentar Cadastrar um novo Registro: ", e)

else:

	try:
		signalUpdate(time.hour)
		print("Novo incremento realizado com Sucesso.")
	except Exception as e:
		print("Erro ao tentar Incrementar um Registro: ", e)
