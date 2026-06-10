import mysql.connector

print("Bienvenidos a la aplicación")

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="portafolioceac"
)

cursor = conexion.cursor()

while True:

    print("\nGESTIÓN DE LIBROS")
    print("1.- Crear libro")
    print("2.- Listar libros")
    print("3.- Actualizar libro")
    print("4.- Eliminar libro")
    print("5.- Salir")

    opcion = input("Elige tu opción: ")

    if opcion == "1":

        titulo = input("Introduce el título: ")
        autor = input("Introduce el autor: ")
        editorial = input("Introduce la editorial: ")

        cursor.execute('''
        INSERT INTO libro
        VALUES (
        NULL,
        "''' + titulo + '''",
        "''' + autor + '''",
        "''' + editorial + '''"
        );
        ''')

        conexion.commit()

        print("Libro creado correctamente")

    elif opcion == "2":

        cursor.execute('''
        SELECT * FROM libro;
        ''')

        filas = cursor.fetchall()

        for fila in filas:
            print(fila)

    elif opcion == "3":

        identificador = input("Introduce el id del libro: ")
        titulo = input("Nuevo título: ")
        autor = input("Nuevo autor: ")
        editorial = input("Nueva editorial: ")

        cursor.execute('''
        UPDATE libro SET
        titulo = "''' + titulo + '''",
        autor = "''' + autor + '''",
        editorial = "''' + editorial + '''"
        WHERE id = ''' + identificador + '''
        ''')

        conexion.commit()

        print("Libro actualizado correctamente")

    elif opcion == "4":

        identificador = input("Introduce el id del libro a eliminar: ")

        cursor.execute('''
        DELETE FROM libro
        WHERE id = ''' + identificador + '''
        ''')

        conexion.commit()

        print("Libro eliminado correctamente")

    elif opcion == "5":

        print("Hasta pronto")
        break

    else:

        print("Opción incorrecta")