import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import existDataInTable1
from sqliteQuerys import cleanContadorFielInTable1

if existDataInTable1() == True:
	try:
		cleanContadorFielInTable1()
		print("Campo (contador) da tabela1 limpo com Sucesso!")
	except Exception as e:
		print("Erro ao tentar Limpar o campo (contador) da Tabela1: ", e)
else:
	print("Nao existe registros na Tabela1: \n execute python saveFakeDataInTable1.py para gerar dados fakes para esta tabela")