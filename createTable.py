import sqlite3
from dataBaseName import dataBaseName

conn = sqlite3.connect(dataBaseName())
cursor = conn.cursor()

# Realiza a criação da tabela do projeto
def createTable(cursor):
	cursor.execute("""
	CREATE TABLE actions (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		quantidade INTEGER,
		linha_producao VARCHAR,
		created_at TIMESTAMP
		);
	""")

# Cria a tabela de Linha de Produção
def createTableLinhaProducao(cursor):
	cursor.execute("""
	CREATE TABLE linhaProducao (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		linha_producao VARCHAR,
		created_at TIMESTAMP
		);
	""")

#createTableLinhaProducao(cursor)
createTable(cursor)