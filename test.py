from sqliteQuerys import selectAllSignals
from sqliteQuerys import setSignalsExportedBYid
from mysqlQuerys import exportDataToExternalDatabase


for row in selectAllSignals():

	try:
		exportDataToExternalDatabase(row[1], row[2], row[3], row[4])
	except Exception as e:
		print("Erro ao tentar Exportar os dados para o Banco remoto.")
		exit()


	try:
		setSignalsExportedBYid(row[0])
	except Exception as e:
		print("Erro ao tentar Setar como (true) os registros que já foram Exportados para o Banco remoto.")