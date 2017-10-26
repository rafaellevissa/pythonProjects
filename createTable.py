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
		linha_producao INT,
		linha_descricao VARCHAR,
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
		linha_producao INT,
		linha_descricao VARCHAR,
		created_at TIMESTAMP
		);
	""")

# Cria a tabela1
def createTable1(cursor):
	cursor.execute("""
	CREATE TABLE tab1 (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		linha INT NOT NULL,
		contador INT NOT NULL,
		meta INT NOT NULL,
		tempo_ciclo INT NOT NULL,
		hora_inicio INT NOT NULL,
		minuto_inicio INT NOT NULL,
		hora_termino INT NOT NULL,
		minuto_termino INT NOT NULL,
		tempo_refresh_realizado INT NOT NULL,
		tempo_refresh_homem INT NOT NULL,
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


try:
    createTable1(cursor)
    print("Tabela tab1 criada com Sucesso!")
except Exception as e:
    print("Erro ao tentar criar a Tabela tab1: ", e)