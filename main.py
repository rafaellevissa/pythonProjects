import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import selectLineProduction
from sqliteQuerys import existSignalFromHour
from sqliteQuerys import signalUpdate
import datetime

signalFromGPIO = 0;

#-------------------------------------------------------------------------------
# Verifica se existe algum registro por hora atual e data atual
#-------------------------------------------------------------------------------
if (existSignalFromHour() != True):

	try:

		signalSave(selectLineProduction())
		print("Novo registro realizado com Sucesso.")

	except Exception as e:
		print("Erro ao tentar Cadastrar um novo Registro: ", e)

else:

	try:

		signalUpdate()
		print("Novo incremento realizado com Sucesso.")

	except Exception as e:
		print("Erro ao tentar Incrementar um Registro: ", e)
#-------------------------------------------------------------------------------