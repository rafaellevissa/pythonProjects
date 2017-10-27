import sqlite3
from sqliteQuerys import deleteExporteds

# Deleta da tabela produção os dados que foram exportados
try:
	deleteExporteds();
	print("Registros Exportados deletados com Sucesso!")
except Exception as e:
	print("Erro ao tentar deletar os arquivos que foram Exportados!", e)