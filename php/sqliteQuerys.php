<?php 
# Quantidade dos Cadeados produzidos no dia
function getLinhaDeProducao($db) 
{
	$_produzidosHoje = $db->query("SELECT linha_producao FROM LinhaProducao");
	return $_produzidosHoje->fetchArray()['linha_producao'];
}