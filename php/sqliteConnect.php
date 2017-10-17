<?php
class Mysqlite extends SQLite3
{
	public function __construct()
	{
		$this->open("../cadeado.db");
	}
}