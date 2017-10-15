<?php 
class Mysqlite extends SQLite3
{
	public function __construct()
	{
		$this->open("../cadeado.db");
	}
}

$db = new Mysqlite();
if ( ! $db) {
	echo $db->lastErrorMsg();
} 

# Array de todos os registros da tabela Produção
$listaProducao = $db->query("SELECT * FROM producao ORDER BY id DESC");

# Quantidade dos Cadeados produzidos no dia
$dataAtual = date('Y-m-d');
$produzidosHoje = $db->query("SELECT SUM(quantidade) AS produzidos FROM producao WHERE created_at = '{$dataAtual}'");