import sqlite3
from dataBaseName import dataBaseName
from sqliteQuerys import saveFakeDataInTable1


try:
   saveFakeDataInTable1()
except Exception as e:
	print("Erro", e)