import sqlite3
from dataBaseName import dataBaseName

conn = sqlite3.connect(dataBaseName())
cursor = conn.cursor()

# Realiza a criação da tabela do projeto
def createTable(cursor):
	cursor.execute("""
	CREATE TABLE actions (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		value INTEGER,
		created_at TIMESTAMP
		);
	""")


createTable(cursor)