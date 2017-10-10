import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import saveLineProduction
from sqliteQuerys import selectLineProduction
import os

def terminalClear():
	os.system('cls' if os.name == 'nt' else 'clear')

def panelOptions():
	terminalClear()

	print("================================================================================================================")
	print("========  PAPAIZ  ==============================================================================================")
   

# Verifica se existe uma Linha de Produção Cadastrada nesse Device
if str(selectLineProduction()) < '1':
	panelOptions()
	getOption = input("Cadastre uma Linha de Producao. [Enter]")
	print("================================================================================================================")
else:
	terminalClear()
	panelOptions()
	print("A Linha de Producao ja foi Cadastrada.")
	exit()


name = ""
while name == "":
    name = input("Digite qual a linha de producao:")


try:

	saveLineProduction(name)
	print("Cadastro realizado com Sucesso.")

except Exception as e:
    print("Error ao tentar cadastrar a linha de producao", e)