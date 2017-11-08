import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import signalSave
from sqliteQuerys import saveLineProduction
from sqliteQuerys import existLineProduction
from terminalClear import terminalClear
import os
from sqliteQuerys import selectLineProduction
from sqliteQuerys import updateLineProductionAndDescritionLineInTable1

def terminalClear():
	os.system('cls' if os.name == 'nt' else 'clear')

def panelOptions():
	terminalClear()

	print("================================================================================================================")
	print("========  PAPAIZ  ==============================================================================================")
   

# Verifica se existe uma Linha de Produção Cadastrada nesse Device
if existLineProduction() == False:
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


#-------------------------------------------------------------------------------
# Salva a linda de produção
#-------------------------------------------------------------------------------
try:
	saveLineProduction(numeroLinhaProducao, descricaoLinha)
	print("Cadastro realizado com Sucesso.")

except Exception as e:
    print("Error ao tentar cadastrar a linha de producao", e)
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Cadastra na tabela 1 o campos (linha) de produção e o campo (descricao_linha)
# selectLineProduction()[0] : Retorna a linda de produção
# selectLineProduction()[1] : Retorna a descrição da linda de produção
#-------------------------------------------------------------------------------
try:
	updateLineProductionAndDescritionLineInTable1(selectLineProduction()[0], selectLineProduction()[1])

except Exception as e:
	print("Erro ao tentar editar os campos (linha) e (linha_descricao) da tabela1", e)
#-------------------------------------------------------------------------------