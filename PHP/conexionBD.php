<?php      

function conectarBD($bdName, $bdUser, $bdPass, $host) {
    try {
        // Establecer la conexión utilizando PDO
        $pdo = new PDO("pgsql:host=$host;dbname=$bdName", $bdUser, $bdPass);

        // Configurar el modo de error de PDO para que lance excepciones en caso de errores
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        return $pdo;
    } catch (PDOException $e) {
        // En caso de error, mostrar el mensaje de error
        echo "Error de conexión: " . $e->getMessage();
        return null;
    }
}

function consultaListadoVentas($conexion, $fechaInicio, $fechaFin) {
    try {
        // Preparar la consulta SQL con la cláusula BETWEEN
        $sql = "SELECT sol.name, so.date_order 
                FROM sale_order_line sol 
                JOIN sale_order so ON sol.order_id = so.id   
                WHERE sol.state = 'sale' 
                AND so.date_order BETWEEN :fechaInicio AND :fechaFin 
                ORDER BY so.date_order";

        // Preparar la sentencia PDO
        $stmt = $conexion->prepare($sql);

        // Enlazar los valores de las fechas como parámetros
        $stmt->bindParam(':fechaInicio', $fechaInicio);
        $stmt->bindParam(':fechaFin', $fechaFin);

        // Ejecutar la consulta
        $stmt->execute();

        // Obtener los resultados
        $resultados = $stmt->fetchAll(PDO::FETCH_ASSOC);

        return $resultados;
    } catch (PDOException $e) {
        $e->getMessage();
        return null;
    }
}

function obtenerLogoCompania($conexion, $companyId) {
    try {
        // Consulta para obtener el logo de la compañía
        $sql = "SELECT logo_web FROM res_company WHERE id = :companyId";

        // Preparar la sentencia PDO
        $stmt = $conexion->prepare($sql);

        // Enlazar el valor del ID de la compañía como parámetro
        $stmt->bindParam(':companyId', $companyId);

        // Ejecutar la consulta
        $stmt->execute();

        // Obtener los datos binarios de la imagen como un string
        $imagenBinaria = $stmt->fetchColumn();

        return $imagenBinaria;

    } catch (PDOException $e) {
        // Manejar errores
        echo "Error al obtener el logo de la compañía: " . $e->getMessage();
        return null;
    }
}



