import sqlite3
from dataBaseName import dataBaseName
import datetime

conn = sqlite3.connect(dataBaseName())
cursor = conn.cursor()


# Salva os valores na tabela actions
def signalSave(hora, lineProduction):

    cursor.execute("""
    INSERT INTO producao (quantidade, linha_producao, hora, created_at)
    VALUES (?,?,?,?)
    """, (1, lineProduction, hora, datetime.datetime.now()))

    conn.commit()
    conn.close()


# Edita o campo Quantidade da tabela Producao
def signalUpdate(hora):
    
    quantidade = getSignalFromHora(hora) + 1

    cursor.execute("""
    UPDATE producao SET quantidade = ? WHERE hora = ?
    """, (quantidade,hora,))

    conn.commit()
    conn.close()


# Retorna o valor do campo Quantidade buscando pelo campo hora
def getSignalFromHora(hora):
    
    hora = str(hora)
    cursor.execute("""SELECT quantidade FROM producao WHERE hora = ?""", (hora,))

    quantidade = 0

    for row in cursor.fetchall():
        quantidade = row[0]

    if (quantidade > 0):
        return quantidade
    else:
        return False


# Verifica se existe algum registro por determinada hora
def existSignalFromHora(hora):
    
    hora = str(hora)
    cursor.execute("""SELECT quantidade FROM producao WHERE hora = ?""", (hora,))

    quantidade = 0

    for row in cursor.fetchall():
        quantidade = row[0]

    if quantidade > 0:
        return True

    return False


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