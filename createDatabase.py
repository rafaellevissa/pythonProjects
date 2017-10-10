import sqlite3
from dataBaseName import dataBaseName

# Cria um banco de dados no diretório local
def createDatabase():
    conn = sqlite3.connect(dataBaseName())
    conn.close()


try:
    createDatabase()
    print("Banco de dados criado com Sucesso!")
except Exception as e:
    print("Erro ao tentar criar o Banco de dados: ", e)
