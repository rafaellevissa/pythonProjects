import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import selectLineProduction
from sqliteQuerys import existSignalFromHour
from sqliteQuerys import signalUpdate
from sqliteQuerys import showMeTheProducaoTable
from sqliteQuerys import existLineProduction
from sqliteQuerys import incrementContadorIntable1
from sqliteQuerys import existDataInTable1
from sqliteQuerys import countToday
from terminalClear import terminalClear
import datetime
import time

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
if  existSignalFromHour() == False:

	try:

		signalSave(selectLineProduction()[0], selectLineProduction()[1])
		print("Novo registro realizado com Sucesso.")
		showMeTheProducaoTable()

	except Exception as e:
		print("Erro ao tentar Cadastrar um novo Registro: ", e)


	if existDataInTable1():
		print('existe')

	else:
		print('nao existe dados na tabela1')

else:

	try:

		signalUpdate()
		print("Novo incremento realizado com Sucesso.")
		showMeTheProducaoTable()

	except Exception as e:
		print("Erro ao tentar Incrementar um Registro: ", e)


	if existDataInTable1():
		incrementContadorIntable1(str(countToday()), selectLineProduction()[1])

	else:
		print('nao existe dados na tabela1')
#-------------------------------------------------------------------------------