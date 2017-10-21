import sqlite3
from sqliteQuerys import deleteExporteds

try:
	deleteExporteds();
	print("Registros Exportados deletados com Sucesso!")
except Exception as e:
	print("Erro ao tentar deletar os arquivos que foram Exportados!", e)