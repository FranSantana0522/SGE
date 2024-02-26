import psycopg2

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

def conexionBD(bdName, bdUser, bdPass, host):
    try:
        conexion = psycopg2.connect(dbname=bdName, user=bdUser, password=bdPass, host=host)
        print("Conexión exitosa a la base de datos")
        return conexion
    except psycopg2.Error as error:
        print("Error al conectarse a la base de datos: ",error)

def consultaBD(conexion, fecha):
    
    resultados_meses = []
    for mes in meses_dict.keys():
        sql = """SELECT sol.name FROM sale_order_line sol 
                 JOIN sale_order so ON sol.order_id=so.id   
                 WHERE sol.state='sale' AND 
                 EXTRACT(MONTH FROM so.date_order) = {} AND 
                 EXTRACT(YEAR FROM so.date_order) = {};""".format(mes, fecha)
        try:
            cursor = conexion.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            resultados_meses.append((mes, resultados))

        except psycopg2.Error as error:
            print("Error al ejecutar la consulta SQL:", error)
        
    return resultados_meses

def ficheros(resultado_meses, fecha):
    for mes_numero, resultados in resultado_meses:
       
        mes_nombre = meses_dict[mes_numero]

        nombre_archivo = f"{fecha}{mes_nombre.lower()}.lst"
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"Ventas para {mes_nombre}:\n")
            for resultado in resultados:
                archivo.write(f"{resultado[0]}\n")



bdName = "2324_SGE_VCF"
bdUser = "odoo"
bdPass = "odoo"
host = "localhost"

fecha = input("Introduce año para listar ventas: ")

if fecha.isdigit():
    fecha=int(fecha)
    conexion = conexionBD(bdName, bdUser, bdPass, host)
    resultado_meses = consultaBD(conexion,fecha)
    ficheros(resultado_meses,fecha)
    
