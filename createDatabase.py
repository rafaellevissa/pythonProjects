import sqlite3

# Cria um banco de dados no diretório local
def createDatabase():
    conn = sqlite3.connect('teste.db')
    conn.close()



createDatabase()