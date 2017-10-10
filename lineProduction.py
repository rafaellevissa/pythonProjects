import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import saveLineProduction

name = ""
while name == "":
	name = input("Digite qual a linha de producao:")

try:
	saveLineProduction(name)
	print("Cadastro realizado com Sucesso.")
	
except Exception as e:
	print("Error ao tentar cadastrar a linha de producao", e)