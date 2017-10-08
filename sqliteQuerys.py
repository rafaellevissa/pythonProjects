import sqlite3
from dataBaseName import dataBaseName
import datetime

conn = sqlite3.connect(dataBaseName())
cursor = conn.cursor()


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