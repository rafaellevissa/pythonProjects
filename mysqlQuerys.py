import pymysql
import sqlite3
from sqliteQuerys import selectAllSignals

conn = pymysql.connect(host = "localhost", user = "root", password = "", db = "just-test")
connect = conn.cursor()

#-------------------------------------------------------------------------------
# Realiza o cadastro dos registros no banco externo
#-------------------------------------------------------------------------------
def exportDataToExternalDatabase(quatidade, linha_producao, hora, created_at):

	connect.execute("""
		INSERT INTO producao (quantidade, linha_producao, hora, created_at)
		VALUES (%s, %s, %s, %s)
		""", (quatidade, linha_producao, hora, created_at))

	conn.commit()
#-------------------------------------------------------------------------------