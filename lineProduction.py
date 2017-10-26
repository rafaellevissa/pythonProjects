import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import saveLineProduction
from sqliteQuerys import selectLineProduction
from terminalClear import terminalClear
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
	getOption = print("Cadastre uma Linha de Producao.")
	print("================================================================================================================")
else:
	terminalClear()
	panelOptions()
	print("A Linha de Producao ja foi Cadastrada.")
	exit()


numeroLinhaProducao = ""
while numeroLinhaProducao == "":
    numeroLinhaProducao = input("Digite qual a linha de producao:")
    
    # Verifica se o valor passado é um Número
    if not numeroLinhaProducao.isdigit():
    	print("*****A Linha de producao deve ser um Numero*****")
    	numeroLinhaProducao = ""


descricaoLinha = ""
while descricaoLinha == "":
	descricaoLinha = input("Digite a descricao da Linha de Producao:")


try:

	saveLineProduction(numeroLinhaProducao, descricaoLinha)
	print("Cadastro realizado com Sucesso.")

except Exception as e:
    print("Error ao tentar cadastrar a linha de producao", e)