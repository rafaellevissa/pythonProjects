import sqlite3
from dataBaseName import dataBaseName

# Cria um banco de dados no diretório local
def createDatabase():
    conn = sqlite3.connect(dataBaseName())
    conn.close()



createDatabase()