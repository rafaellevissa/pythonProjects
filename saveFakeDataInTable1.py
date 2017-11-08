import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import saveFakeDataInTable1
from sqliteQuerys import selectLineProduction
from sqliteQuerys import existDataInTable1


#-------------------------------------------------------------------------------
# Cadastra dados fakes na tabela1. Obs: Os unicos dados reais que são cadastrados são os campos (linha) de produção e o campo (descricao_linha)
# selectLineProduction()[0] : Retorna a linda de produção
# selectLineProduction()[1] : Retorna a descrição da linda de produção
#-------------------------------------------------------------------------------
try:
   if existDataInTable1() == False:
    saveFakeDataInTable1(selectLineProduction()[0], selectLineProduction()[1])
   else:
   	print("Ja existe registro na Tabela1")

except Exception as e:
	print("Erro", e)