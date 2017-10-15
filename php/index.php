<?php require_once('database.php');?>

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

		<div class="col-lg-4 content-table" align="center">

			<div class="table-responsive" style="padding:10px">
				<b>Produzidos Hoje</b>
				<h1 class="number"><?php echo $produzidosHoje->fetchArray()['produzidos'];?></h1>
			</div>
			
		</div>

		<div class="col-lg-8 content-table" align="center">

			<div class="table-responsive" style="padding:10px">
				<table class="table table-striped table-bordered">
					<tr>
						<th>Produzidos</th>
						<th>Linha de Produção</th>
						<th>Hora</th>
						<th>Data</th>
						<th>Exportado</th>
				    </tr>

				    <?php while ($row = $listaProducao->fetchArray()):?>
				    	<tr>
				    		<td><?php echo $row["quantidade"];?></td>
				    		<td><?php echo $row["linha_producao"];?></td>
				    		<td><?php echo $row["hora"]."h"?></td>
				    		<td><?php echo date('d/m/Y', strtotime($row["created_at"]));?></td>
				    		<td><?php echo isset($row["enviado"]) ? "SIM" : "NÃO";?></td>
				    	</tr>
				    <?php endwhile;?>
		       </table>
			</div>
			
		</div>
		
	</div>
</div>

<?php $db->close(); ?>

<script src="js/jquery.js"></script>
<script src="js/bootstrap.min.js"></script>

<script type="text/javascript">

	function atualizar() {
	  location.reload(true)
	}

   window.setInterval("atualizar()",10000);

</script>

</body>
</html>