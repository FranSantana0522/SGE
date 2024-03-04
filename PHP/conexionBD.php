<?php      

// Funcion para conectar con la base de datos
function conectarBD($bdName, $bdUser, $bdPass, $host) {
    try {
        // Establecer la conexión utilizando PDO
        $pdo = new PDO("pgsql:host=$host;dbname=$bdName", $bdUser, $bdPass);

        // Configurar el modo de error de PDO para que lance excepciones en caso de errores
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        return $pdo;
    } catch (PDOException $e) {
        // En caso de error mostrar el mensaje de error
        echo "Error de conexión: " . $e->getMessage();
        return null;
    }
}

// Funcion para hacer la consulta a la base de datos
function consultaListadoVentas($conexion, $fechaInicio, $fechaFin) {
    try {
        // Consulta sql para recoger el listado de ventas entre dos fechas
        $sql = "SELECT sol.name, so.date_order 
                FROM sale_order_line sol 
                JOIN sale_order so ON sol.order_id = so.id   
                WHERE sol.state = 'sale' 
                AND so.date_order BETWEEN :fechaInicio AND :fechaFin 
                ORDER BY so.date_order";

        // Preparar la sentencia
        $stmt = $conexion->prepare($sql);

        // Enlazar los valores de las fechas con los parametros
        $stmt->bindParam(':fechaInicio', $fechaInicio);
        $stmt->bindParam(':fechaFin', $fechaFin);

        // Ejecutar la consulta
        $stmt->execute();

        // Obtenemos los resultados
        $resultados = $stmt->fetchAll(PDO::FETCH_ASSOC);

        return $resultados;
    } catch (PDOException $e) {
        $e->getMessage();
        return null;
    }
}



