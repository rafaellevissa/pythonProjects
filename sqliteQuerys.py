import sqlite3
from dataBaseName import dataBaseName
import datetime

conn = sqlite3.connect(dataBaseName())
cursor = conn.cursor()


# Salva os valores na tabela actions
def signalSave(quantidade, lineProduction):

    cursor.execute("""
    INSERT INTO actions (quantidade, linha_producao, created_at)
    VALUES (?,?,?)
    """, (quantidade, lineProduction, datetime.datetime.now()))

    conn.commit()
    conn.close()

# Salva os valores na tabela actions
def signalSave(signalValue):

    cursor.execute("""
    INSERT INTO actions (value, created_at)
    VALUES (?,?)
    """, (signalValue, datetime.datetime.now()))

    conn.commit()
    conn.close()

# Retorna a quantidade de registros cadastrados no banco
def signalsCount():

	cursor.execute("""SELECT COUNT(*) FROM actions""")

	signalCount = 0

	for row in cursor.fetchall():
		signalCount = row[0]

	return signalCount

# Cadastra a Linha de Produção
def saveLineProduction(lineProduction):

    cursor.execute("""
    INSERT INTO linhaProducao (linha_producao, created_at)
    VALUES (?,?)
    """, (lineProduction, datetime.datetime.now()))

    conn.commit()
    conn.close()

# Seleciona a Linha de Produção cadastrada
def selectLineProduction():

    cursor.execute("""SELECT * FROM linhaProducao LIMIT 1""")

    lineProduction = ""

    for row in cursor.fetchall():
        lineProduction = row[1]

    return lineProduction