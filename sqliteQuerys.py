import sqlite3
from dataBaseName import dataBaseName
from terminalClear import terminalClear
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
def signalSave(lineProduction, descriptionLineProduction):

    hora = str(time.hour)

    cursor.execute("""
    INSERT INTO producao (quantidade, linha_producao, linha_descricao, hora, created_at)
    VALUES (?,?,?,?,?)
    """, (1, lineProduction, descriptionLineProduction, hora, myDateFormat()))

    conn.commit()
    #conn.close()

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
    #conn.close()
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
def saveLineProduction(lineProduction, descriptionLineProduction):

    cursor.execute("""
    INSERT INTO linhaProducao (linha_producao, linha_descricao, created_at)
    VALUES (?,?,?)
    """, (lineProduction, descriptionLineProduction, myDateFormat()))

    conn.commit()
    #conn.close()
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Verifica se Existe uma linha de Produção cadastrada
#-------------------------------------------------------------------------------
def existLineProduction():

    cursor.execute("""
    SELECT COUNT(*) FROM linhaProducao
    """)

    quantidade = 0

    for row in cursor.fetchall():
        quantidade = row[0]

    if quantidade > 0:
        return True

    return False
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Seleciona a Linha de Produção cadastrada
# Return : O valor do campo linha_produção da tabela Produção
#-------------------------------------------------------------------------------
def selectLineProduction():

    cursor.execute("""SELECT * FROM linhaProducao LIMIT 1""")

    lineProduction = ""
    descriptionLineProduction = ""

    for row in cursor.fetchall():
        lineProduction = row[1]
        descriptionLineProduction = row[2]

    return [lineProduction, descriptionLineProduction]
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Verifica se Já existe uma Linha de produção cadastrada
# Return : True or False
#-------------------------------------------------------------------------------
def existLineProduction():

    cursor.execute("""SELECT id FROM linhaProducao""")

    count = 0;

    for row in cursor.fetchall():
        count = row[0]

    if count > 0:
        return True

    return False
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



#-------------------------------------------------------------------------------
# Apresenta todos os Registros cadastrados na tabela Produção
#-------------------------------------------------------------------------------
def showMeTheProducaoTable():

    cursor.execute("""SELECT * FROM producao ORDER BY created_at ASC, hora DESC""")
    
    terminalClear()

    print("-------------------------------------------------------------------------------------")
    print("REGISTROS CADASTRADOS NA TABELA PRODUCAO")
    print("-------------------------------------------------------------------------------------")

    for row in cursor.fetchall():
        quantidade = "0" + str(row[1]) if row[1] < 10 else str(row[1])

        print("id: " + str(row[0]) + " | quantidade: " + quantidade + " | linha producao: " + str(row[2]) + " | descricao: " + str(row[3]) + " | hora: " + str(row[4]) + " | data: " + str(row[5]) + " | enviado: " + str(row[6]))
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Apresenta a soma de todos os Registros cadastrados na tabela Produção. 
# Obs: Registros do dia
# return: INT 
#-------------------------------------------------------------------------------
def countToday():

    cursor.execute("""SELECT SUM(quantidade) AS produzidos FROM producao WHERE created_at = ?""", (myDateFormat(),))
    
    data = 0
    for row in cursor.fetchall():
        data = row[0]

    return data
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Salva os registros na tabela Produção
#-------------------------------------------------------------------------------
def deleteExporteds():

    cursor.execute("""
    DELETE FROM producao WHERE enviado IS NOT NULL
    """)

    conn.commit()
    #conn.close()

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Verifica se existe registros na tabela1
# return: True or False
#-------------------------------------------------------------------------------
def existDataInTable1():

    cursor.execute("""SELECT id from tab1""")

    quantidade = 0;

    for row in cursor.fetchall():
        quantidade = row[0]

    if quantidade > 0:
        return True

    return False
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Salva os registros na tabela1
#-------------------------------------------------------------------------------
def incrementContadorIntable1(countToday, descriptionLineProduction):

    cursor.execute("""UPDATE tab1 SET contador = ?, descricao_linha = ?""", (countToday, descriptionLineProduction,))

    conn.commit()
    #conn.close()

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Edita os campos linha e descricao_linha da tabela1
#-------------------------------------------------------------------------------
def updateLineProductionAndDescritionLineInTable1(lineProduction, descritionLineProduction):

    cursor.execute("""UPDATE tab1 SET linha = ?, descricao_linha = ?""", (lineProduction, descritionLineProduction,))

    conn.commit()
    #conn.close()

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Zera o campo contador da tabela 1
#-------------------------------------------------------------------------------
def cleanContadorFielInTable1():

    cursor.execute("""UPDATE tab1 SET contador = ?""", (0,))

    conn.commit()
    #conn.close()

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Popula inicialmente a tabela1
#-------------------------------------------------------------------------------
def saveFakeDataInTable1(lineProduction, descritionLine):
    cursor.execute("""
        INSERT INTO tab1 
        (linha, 
         descricao_linha,
         contador,
         meta,
         tempo_ciclo,
         hora_inicio,
         minuto_inicio,
         hora_termino,
         minuto_termino,
         tempo_refresh_realizado,
         tempo_refresh_homem,
         created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            lineProduction,
            descritionLine,
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',
            '00',
            '0',
            '0000-00-00 00:00:00'
            ))

    conn.commit()
    #conn.close()
