<?php 
date_default_timezone_set('America/Bahia');

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

# Quantidade dos Cadeados produzidos no dia
if (isset($_GET['getProduced'])) {

	$dataAtual = date('Y-m-d');
	$_produzidosHoje = $db->query("SELECT SUM(quantidade) AS produzidos FROM producao WHERE created_at = '{$dataAtual}'");
	echo json_encode($_produzidosHoje->fetchArray()['produzidos']);
	$db->close();

}