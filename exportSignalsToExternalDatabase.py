from sqliteQuerys import selectAllSignals
from sqliteQuerys import setSignalsExportedBYid
from mysqlQuerys import exportDataToExternalDatabase

#-------------------------------------------------------------------------------
# Realiza a exportação dos registros da base local para o banco de dados remoto
#-------------------------------------------------------------------------------
for row in selectAllSignals():
    
    # Tenta gravar os dados no Banco de dados remoto
    # row[1] = quantidade
    # row[2] = linha de produção
    # row[3] = descrição da linha de produção
    # row[4] = hora do cadastro do registro
    # row[5] = ano-mes-dia do cadastro do registro
	try:
		exportDataToExternalDatabase(row[1], row[2], row[3], row[4], row[5])
	except Exception as e:
		print("Erro ao tentar Exportar os dados para o Banco remoto.")
		exit()

    # Tenta marcar como enviado todos os registros que de fato foram exportados
    # row[0] = Id dos registro enviados
	try:
		setSignalsExportedBYid(row[0])
	except Exception as e:
		print("Erro ao tentar Setar como (true) os registros que já foram Exportados para o Banco remoto.")
#-------------------------------------------------------------------------------