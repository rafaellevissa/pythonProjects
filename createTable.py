import sqlite3
from dataBaseName import dataBaseName

conn = sqlite3.connect(dataBaseName())
cursor = conn.cursor()

# Realiza a criação da tabela do projeto
def createTableProducao(cursor):
	cursor.execute("""
	CREATE TABLE producao (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		quantidade INTEGER,
		linha_producao VARCHAR,
		hora VARCHAR,
		created_at VARCHAR,
		enviado VARCHAR DEFAULT NULL
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

try:
    createTableLinhaProducao(cursor)
    print("Tabela Linha de producao criada com Sucesso!")
except Exception as e:
    print("Erro ao tentar criar a Tabela Linha de producao: ", e)


try:
    createTableProducao(cursor)
    print("Tabela Producao criada com Sucesso!")
except Exception as e:
	print("Erro ao tentar criar a Tabela Producao: ", e)