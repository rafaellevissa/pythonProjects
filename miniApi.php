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


$dataAtual = date('Y-m-d');
$produzidosHoje = $db->query("SELECT SUM(quantidade) AS produzidos FROM producao WHERE created_at = '{$dataAtual}'");

echo $produzidosHoje;