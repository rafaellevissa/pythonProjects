import sqlite3
from sqliteQuerys import selectAllSignals
from mysqlConnect import connect

conn = connect()
connect = conn.cursor()

#-------------------------------------------------------------------------------
# Realiza o cadastro dos registros no banco externo
#-------------------------------------------------------------------------------
def exportDataToExternalDatabase(quatidade, linha_producao, linha_descricao, hora, created_at):

	created_at = created_at + " " + str(hora) + ":00:00"

	connect.execute("""
		INSERT INTO producao (quantidade, linha_producao, linha_descricao, hora, created_at)
		VALUES (%s, %s, %s, %s, %s)""", (quatidade, linha_producao, linha_descricao, hora, created_at))

	conn.commit()
#-------------------------------------------------------------------------------