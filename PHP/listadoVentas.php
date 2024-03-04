<?php
// Verificar si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Verificar si se han recibido los campos del formulario
    if (isset($_POST['formId1']) && isset($_POST['formId2'])) {
        // Recoger los valores de los campos del formulario
        $fechaInicio = $_POST['formId1'];
        $fechaFin = $_POST['formId2'];

        // Incluir el archivo con las funciones de conexión y consulta
        include 'conexionBD.php';
        $bdName = "2324_SGE_VCF";
        $bdUser = "odoo";
        $bdPass = "odoo";
        $host = "localhost";
        // Conectar a la base de datos
        $conexion = conectarBD($bdName, $bdUser, $bdPass, $host);

        if ($conexion) {
            // Ejecutar la consulta
            $resultados = consultaListadoVentas($conexion, $fechaInicio, $fechaFin);

            // Cerrar la conexión
            $conexion = null;

            // Mostrar los resultados en una tabla
            ?>
            <!doctype html>
            <html lang="en">
            <head>
                <title>Listado de ventas</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            </head>
            <body class="bg-warning">
                <div class="wrapper">
                    <header class="bg-dark text-light d-flex align-items-center" style="height:10vh">
                        <div class="container-auto">
                            <img src='./san-francisco-california-skyline-6.jpg' alt='Logo de la compañía' class="fixed-left img-fluid" style="width: 200px; height: 10vh;">
                        </div>
                        <div class="container-fluid text-center d-flex align-items-center justify-content-center me-5" style="height:10vh">
                            <h1 class="me-5">Listado de ventas</h1>
                        </div>
                    </header>

                    <main class="mb-5">
                        <div class="container mt-3 ">
                            <div class="row justify-content-center">
                                <div class="col-md-8">
                                    <?php
                                    if (empty($_POST['formId1']) || empty($_POST['formId2'])) {
                                        echo "<div class='alert alert-danger' role='alert'>";
                                        echo "Error: Uno o más campos del formulario están vacíos.";
                                        echo "</div>";
                                        echo "<div class='text-center mb-3'>";
                                        echo "<a href='index.php' class='btn btn-primary'>Volver</a>";
                                        echo "</div>";
                                    } else {
                                        if (!empty($resultados)) :
                                            ?>
                                            <table class="table table-dark text-light">
                                                <thead class="thead-dark">
                                                    <tr>
                                                        <th scope="col">Nombre</th>
                                                        <th scope="col">Fecha de orden</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <?php foreach ($resultados as $venta) : ?>
                                                        <tr>
                                                            <td><?= $venta['name'] ?></td>
                                                            <td><?= $venta['date_order'] ?></td>
                                                        </tr>
                                                    <?php endforeach; ?>
                                                </tbody>
                                            </table>
                                            <div class="text-center mb-5">
                                                <a href="index.php" class="btn btn-primary">Volver</a>
                                            </div>
                                        <?php else : ?>
                                            <div class="alert alert-info" role="alert">
                                                No se encontraron ventas para el rango de fechas especificado.
                                            </div>
                                            <div class="text-center">
                                                <a href="index.php" class="btn btn-primary">Volver</a>
                                            </div>
                                        <?php endif;
                                    }
                                    ?>

                                </div>
                            </div>
                        </div>
                    </main>
                    <footer class="bg-dark text-light fixed-bottom py-4" style="height:10vh">
                    <?php
                    // Mostrar el footer solo si hay resultados
                    if (!empty($resultados)) {
                        ?>
                            <div class="container text-center">
                                Informe generado el <?= date("Y-m-d H:i:s") ?>
                            </div>   
                    <?php } ?>
                    </footer>
                </div>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
            </body>
            </html>
            <?php
        }
    }
}
?>
