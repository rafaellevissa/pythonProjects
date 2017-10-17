<?php 
require_once('sqliteConnect.php');
require_once('sqliteQuerys.php');

$db = new Mysqlite();

if ( ! $db) {
	echo $db->lastErrorMsg();
} 
?>

<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Produzidos</title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>


<div class="container">
    
    <div class="row">
		<div class="col-lg-12 content-top">
			<img src="img/logo.jpg" width="150">
		</div>
    </div>

	<div class="row">

		<div class="col-lg-12 content-table" align="center">

			<div class="table-responsive" style="padding:10px">
				<span>Hora atual:</span>
				<br>
				<b class="hora_atual" style="font-size:20px"></b> <br>

                <h5>
                	Linha de Produção: 
                	<span style="color:#ff6600;"><?php echo getLinhaDeProducao($db);?></span>
                </h5>

                <h3>Cadeados produzidos até o momento</h3>
				
				<hr>
				<h1 class="number"></h1>
			</div>
			
		</div>

	</div>
</div>

<script src="js/jquery.js"></script>
<script src="js/bootstrap.min.js"></script>

<script>

   $(function() {

	   	function _getJsonCadeadosProduzidosNoDia() {

	   	  	$.getJSON("miniApi.php?getProduced", function(result) {
			    var obj = JSON.parse(result)
			    if (obj == null) {
			    	$(".number").text("0");
			    } else {
			    	$(".number").text(obj);
			    }
			   	
			});
	   	}

	   	var time = setInterval(function() {
		   	_getJsonCadeadosProduzidosNoDia();
	   	}, 200);

	   	function horaAtual() {
	   		var hora_atual =  new Date();
	   		$(".hora_atual").text(hora_atual.getHours() + " : " + hora_atual.getMinutes() + " : " + hora_atual.getSeconds());
	   	}

	   	var time = setInterval(function() {
		   	horaAtual()
	   	}, 0000);
	
   });

</script>

</body>
</html>