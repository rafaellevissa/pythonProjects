import sqlite3
from dataBaseName import dataBaseName
import datetime

conn = sqlite3.connect(dataBaseName())
cursor = conn.cursor()
time = datetime.datetime.now()



#-------------------------------------------------------------------------------
# Cria uma data no formato Y-m-d
#-------------------------------------------------------------------------------
def myDateFormat():
    return str(time.year) + "-" + str(time.month) + "-" + str(time.day)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Salva os registros na tabela Produção
#-------------------------------------------------------------------------------
def signalSave(lineProduction):

    hora = str(time.hour)

    cursor.execute("""
    INSERT INTO producao (quantidade, linha_producao, hora, created_at)
    VALUES (?,?,?,?)
    """, (1, lineProduction, hora, myDateFormat()))

    conn.commit()
    conn.close()

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Edita o campo Quantidade da tabela Produçao sempre incrementando 1
#-------------------------------------------------------------------------------
def signalUpdate():
    
    quantidade = getSignalFromHourAndDate() + 1

    hora = str(time.hour)

    cursor.execute("""
    UPDATE producao SET quantidade = ? WHERE hora = ? AND enviado IS NULL
    """, (quantidade,hora,))

    conn.commit()
    conn.close()
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Retorna O valor do campo Quantidade buscando pelo campo Hora atual e Data atual da tabela Produção
# Return : O valor do campo Quantidade
#-------------------------------------------------------------------------------
def getSignalFromHourAndDate():
    
    hora = str(time.hour)

    cursor.execute("""SELECT quantidade FROM producao WHERE hora = ? AND created_at = ?""", (hora, myDateFormat(),))

    quantidade = 0

    for row in cursor.fetchall():
        quantidade = row[0]

    if (quantidade > 0):
        return quantidade
    else:
        return False
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Verifica se existe algum registro por Hora atual e Data atual da tabela Produção
# Return : True ou False
#-------------------------------------------------------------------------------
def existSignalFromHour():
    
    hora = str(time.hour)
    cursor.execute("""SELECT quantidade FROM producao WHERE hora = ? AND created_at = ?""", (hora, myDateFormat(),))

    quantidade = 0

    for row in cursor.fetchall():
        quantidade = row[0]

    if quantidade > 0:
        return True

    return False
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Cadastra a Linha de Produção
#-------------------------------------------------------------------------------
def saveLineProduction(lineProduction):

    cursor.execute("""
    INSERT INTO linhaProducao (linha_producao, created_at)
    VALUES (?,?)
    """, (lineProduction, myDateFormat()))

    conn.commit()
    conn.close()
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Seleciona a Linha de Produção cadastrada
# Return : O valor do campo linha_produção da tabela Produção
#-------------------------------------------------------------------------------
def selectLineProduction():

    cursor.execute("""SELECT * FROM linhaProducao LIMIT 1""")

    lineProduction = ""

    for row in cursor.fetchall():
        lineProduction = row[1]

    return lineProduction
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Seleciona todos os registros que ainda não foram exportados
# Return : Tupla com todos os registro
#-------------------------------------------------------------------------------
def selectAllSignals():

    cursor.execute("""SELECT * FROM producao WHERE enviado is null""")
    return cursor.fetchall()
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Seta os registros que já foram exportados
#-------------------------------------------------------------------------------
def setSignalsExportedBYid(id):
    
    cursor.execute("""
    UPDATE producao SET enviado = ? WHERE id = ?
    """, ("true", id,))

    conn.commit()
#-------------------------------------------------------------------------------

# Apenas me mostra uma Tupla dos registros
def showMeTheProducaoTable():
    cursor.execute("""SELECT * FROM producao WHERE enviado is null""")
    return cursor.fetchall()