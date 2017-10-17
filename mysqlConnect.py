import pymysql

# Retorna a conexão com a base de dados Mysql
def connect():
	return pymysql.connect(host = "", user = "root", password = "", db = "")