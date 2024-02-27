import argparse # Import para pasar argumentos a la app desde la linea de comandos
import psycopg2 # Import para la conexion con la base de datos postgres

# Diccionario para los meses del año 
meses_dict = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

# Funcion para la conexion a la base de datos
def conexionBD(bdName, bdUser, bdPass, host):
    try:
        # Conectamos con la base de datos de postgres y la devolvemos
        conexion = psycopg2.connect(dbname=bdName, user=bdUser, password=bdPass, host=host)
        return conexion
    except psycopg2.Error as error:
        print("Error al conectarse a la base de datos: ",error)

# Funcion para la consulta a la base de datos
def consultaBD(conexion, fecha):
    
    # Array con los resultados de cada mes
    resultados_meses = []
    for mes in meses_dict.keys():
        # Listamos todos los productos vendidos del año pasado como parametro y de cada mes de ese año en orden creciente
        sql = """SELECT sol.name,so.date_order FROM sale_order_line sol 
                 JOIN sale_order so ON sol.order_id=so.id   
                 WHERE sol.state='sale' AND 
                 EXTRACT(MONTH FROM so.date_order) = {} AND 
                 EXTRACT(YEAR FROM so.date_order) = {} ORDER BY so.date_order;""".format(mes, fecha)
        try:
            # Se crea un cursor para realizar la sentencia
            cursor = conexion.cursor()
            # Ejecutamos la consulta
            cursor.execute(sql)
            # Devuelve una lista de tuplas con las filas de los resultados
            resultados = cursor.fetchall()
            # Se lo añadimos al array de meses los resultados
            resultados_meses.append((mes, resultados))

        except psycopg2.Error as error:
            print("Error al ejecutar la consulta SQL:", error)
        
    return resultados_meses

# Funcion para escribir los ficheros
def ficheros(resultado_meses, fecha):
    for mes_numero, resultados in resultado_meses:
       
        # Obtenemos el nombre del diccionario de meses
        mes_nombre = meses_dict[mes_numero]
        
        # Asignamos el nombre del fichero con el año y el mes listado
        nombre_archivo = f"{fecha}{mes_nombre.lower()}.lst"
        # Abrimos el fichero en escritura y escribimos una cabezera y el contenido del array de la consulta 
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"Ventas para {mes_nombre}:\n")
            for resultado in resultados:
                archivo.write(f"{resultado[1]}: {resultado[0]}\n")
    print("Se han generado los ficheros exitosamente")

# Main
if __name__ == "__main__":
    # Instanciamos el argparse para poder recibir argumentos desde la linea de comandos
    parser = argparse.ArgumentParser()
    # Añadimos un argumento de tipo int llamado year
    parser.add_argument("year", type=int)
    # Le pasamos a una variable el argumento
    args = parser.parse_args()

    bdName = "2324_SGE_VCF"
    bdUser = "odoo"
    bdPass = "odoo"
    host = "localhost"
    # Obtenemos el contenido del argumento
    fecha = args.year #input("Introduce año para listar ventas: ")
    
    # Llamada al metodo para la conexion
    conexion = conexionBD(bdName, bdUser, bdPass, host)
    # Llamada al metodo para la consulta
    resultado_meses = consultaBD(conexion,fecha)
    # Llamada al metodo para generar los ficheros 
    ficheros(resultado_meses,fecha)
    
