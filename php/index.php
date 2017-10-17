<!DOCTYPE html>
<html>
<head>
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
				<b class="hora_atual" style="font-size:20px"></b>

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
	   	  	$.getJSON("database.php?getProduced", function(result) {
			    var obj = JSON.parse(result)
			   	$(".number").text(obj);
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