import pymysql

def connect():
	return pymysql.connect(host = "teste.wifiaqui.com.br", user = "root", password = "mysql.xlogic", db = "just-test")