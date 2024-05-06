import sqlite3
from datetime import datetime, timedelta
from tabulate import tabulate
lista_pacientes = []
lista_citas = []

def conectar_base_datos():
    conn = sqlite3.connect('CONSULTORIO.db')
    return conn

def crear_tablas(conn):
    try:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Pacientes(Clave_pac INTEGER PRIMARY KEY, PRIMER_APELLIDO TEXT NOT NULL, SEGUNDO_APELLIDO TEXT NOT NULL, NOMBRE TEXT NOT NULL, FECHA_DE_NACIMIENTO TEXT, SEXO TEXT NOT NULL)")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Citas (Folio_cita INTEGER PRIMARY KEY, Clave_pac INTEGER, FECHA_CITA TEXT NOT NULL, Turno_cita INTEGER, FOREIGN KEY (Clave_pac) REFERENCES Pacientes(Clave_pac))")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Reportes_y_consultas (Folio_cita INTEGER, Clave_pac INTEGER, Hora_llegada TEXT NOT NULL, Peso_kg REAL NOT NULL, Estatura_cm REAL NOT NULL, Presion_sistolica INTEGER NOT NULL, Presion_diastolica INTEGER NOT NULL, Diagnostico TEXT NOT NULL CHECK(LENGTH(Diagnostico) <= 200), FOREIGN KEY(Folio_cita) REFERENCES Citas(Folio_cita), FOREIGN KEY(Clave_pac) REFERENCES Pacientes(Clave_pac))")
        conn.commit()
        return mi_cursor
    except sqlite3.Error as e:
        print("Error de SQLite:", e)
    except Exception as e:
        print("Se produjo el siguiente error:", e)

def generar_clave(mi_cursor):
    mi_cursor.execute("SELECT COUNT(*) FROM Pacientes")
    count = mi_cursor.fetchone()[0]
    if count is None:
        return 1
    return count + 1

def validar_fecha(fecha):
    fecha_actual = datetime.now()
    fecha_maxima = fecha_actual + timedelta(days=60)
    if fecha < fecha_actual or fecha > fecha_maxima:
        return False
    if fecha.weekday() == 6:  
        print("La fecha programada cae en domingo. Se programará para el sábado posterior.")
        fecha = fecha - timedelta(days=1)
    return fecha
       
def registrar_paciente(conn, mi_cursor, lista_pacientes):
    mi_cursor = conn.cursor()
    
    while True:
        primerapellido = input("Ingresa tu primer apellido: ").capitalize().strip()

        if primerapellido.lower() == 'x':  
            print("Saliendo...")
            return  

        if not primerapellido:
            print('No se puede quedar en blanco el primer apellido, INTENTE DE NUEVO')
            continue
        elif primerapellido.isdigit():
            print('El primer apellido no puede ser un numero, INTENTE DE NUEVO')
            continue
        else:
            break

    segundoapellido = ""
    while True:
        segundoapellido = input("Ingresa tu segundo apellido: ").capitalize().strip()

        if segundoapellido.lower() == 'x': 
            print("Saliendo...")
            return 

        if segundoapellido.isdigit():
            print('El segundo apellido no puede ser un numero, INTENTE DE NUEVO')
            continue
        else:
            break

    nombre = ""
    while True:
        nombre = input("Ingresa tu nombre: ").capitalize().strip()

        if nombre.lower() == 'x':  
            print("Saliendo...")
            return  
        if not nombre:
            print('NO SE PUEDE QUEDAR EL NOMBRE EN BLANCO, INTENTE DE NUEVO')
            continue
        elif nombre.isdigit():
            print('EL NOMBRE NO PUEDE SER UN NÚMERO, INTENTE DE NUEVO')
            continue
        else:
            break

    fecha_nacimiento = None
    while True:
        fecha_nac = input("Por favor, ingrese una fecha de nacimiento (formato: mm/dd/aaaa): ")

        if fecha_nac.lower() == 'x':  
            print("Saliendo...")
            return  

        try:
            fecha_procesada = datetime.strptime(fecha_nac, "%m/%d/%Y")
            if fecha_procesada < datetime.now():
                fecha_nacimiento = fecha_procesada
                break
            else:
                print("La fecha ingresada es en el futuro. Por favor, intente de nuevo.")
        except ValueError:
            print("Formato de fecha inválido. Por favor, ingrese la fecha en el formato mm/dd/aaaa.")

    
    
    while True:
        sexo = input("Ingresa tu sexo ((H)ombre, (M)ujer, (N)o contestó): ").upper()

        if sexo.lower() == 'x':  
            print("Saliendo...")
            return  

        if sexo not in ['H', 'M', 'N']:
            print('Opción no válida. Por favor, elige una de las opciones proporcionadas.')
            continue
        else:
            break
    
    clave = generar_clave(mi_cursor)
    try:
        mi_cursor.execute("INSERT INTO Pacientes (Clave_pac, PRIMER_APELLIDO, SEGUNDO_APELLIDO, NOMBRE, FECHA_DE_NACIMIENTO, SEXO) VALUES (?, ?, ?, ?, ?, ?)",
                          (clave, primerapellido, segundoapellido, nombre, fecha_nacimiento, sexo))
        conn.commit()
        print("\nDatos del paciente registrado:")
        print(tabulate([[clave, primerapellido, segundoapellido, nombre, fecha_nacimiento.strftime('%m/%d/%Y'), sexo]],
                       headers=["Clave", "Primer Apellido", "Segundo Apellido", "Nombre", "Fecha de Nacimiento", "Sexo"],
                       tablefmt="plain"))
    except sqlite3.Error as e:
        print("Error al registrar el paciente en la base de datos:", e)
        
def submenu_programar_cita(conn):
    while True:
        print("\n*** Submenú Programar Cita ***")
        print("1. Programar cita")
        print("2. Realización de citas programadas")
        print("3. Cancelación de citas")
        print("4. Volver al menú principal")
        print()
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            capturar_datos_cita(conn)
        elif opcion == '2':
            realizar_cita(conn)
        elif opcion == '3':
            cancelar_cita(conn)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            
def generar_folio():
    return str(int(datetime.now().strftime('%y%m%d%H%M%S')) % 100).zfill(2)

def obtener_fecha_disponible():
    hoy = datetime.now()
    fecha_maxima = hoy + timedelta(days=60)
    if fecha_maxima.weekday() == 6: 
        fecha_maxima -= timedelta(days=1)  
    return fecha_maxima.strftime('%m/%d/%Y')

def capturar_datos_cita(conn):
    mi_cursor = conn.cursor()

    while True:
        try:
            clave_paciente = int(input("Ingrese la clave del paciente: "))
        except ValueError:
            print("Error: Debe ingresar un número entero. Intente de nuevo.")
            continue
        
        
        mi_cursor.execute("SELECT Clave_pac FROM Pacientes WHERE Clave_pac = ?", (clave_paciente,))
        paciente_existente = mi_cursor.fetchone()
        if not paciente_existente:
            print("Clave de paciente no válida. Intente de nuevo.")
            continue
        else:
            break
    
    folio_cita = generar_folio()
    print("Fecha disponible más lejana:", obtener_fecha_disponible())
    while True:
        fecha_cita = input("Ingrese la fecha de la cita (mm/dd/aaaa): ")
        try:
            fecha_cita = datetime.strptime(fecha_cita, '%m/%d/%Y')
            if datetime.now() <= fecha_cita <= datetime.now() + timedelta(days=60):
                if fecha_cita.weekday() == 6: 
                    print("La fecha cae en domingo. Se programará para el sábado inmediato antes de la fecha deseada.")
                    fecha_cita -= timedelta(days=1)
                break
            else:
                raise ValueError
        except ValueError:
            print("La fecha debe ser posterior al día actual y no mayor a 60 días en el futuro.")

    while True:
        turno_cita = input("Ingrese el turno de la cita (1 - mañana, 2 - mediodía, 3 - tarde): ")
        if turno_cita.isdigit() and int(turno_cita) in [1, 2, 3]:
            turno_cita = int(turno_cita)
            break
        else:
            print("Error: Debe ingresar un número entero entre 1 y 3. Intente de nuevo.")

    try:
        mi_cursor.execute("INSERT INTO Citas (Folio_cita, Clave_pac, FECHA_CITA, Turno_cita) VALUES (?, ?, ?, ?)",
                          (folio_cita, clave_paciente, fecha_cita.strftime('%Y-%m-%d'), turno_cita))
        conn.commit()
        print("\nCita registrada con éxito.")
    except sqlite3.Error as e:
        print("Error al registrar la cita:", e)

        
def menu_principal():
    conn = conectar_base_datos()
    mi_cursor = crear_tablas(conn)
    
    opcion_uno_seleccionada = False  
    
    while True: 
        print("\n*** Menú Principal ***")
        print("1. Registrar paciente")
        print("2. Programar cita")
        print("3. Reporte de citas")
        print("4. Guardar datos en archivo CSV")
        print("5. Cargar datos desde archivo CSV")
        print("6. Salir")
        print()
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_paciente(conn, mi_cursor, lista_pacientes)
            opcion_uno_seleccionada = True  
        elif opcion == '2' and opcion_uno_seleccionada:
            submenu_programar_cita(conn)
        elif opcion == '3':
            submenu_reporte_citas(conn)
        elif opcion == '4':
            guardar_datos_en_csv()
        elif opcion == '5':
            cargar_datos_desde_csv()
        elif opcion == '6':
            confirmacion = input("¿Está seguro que desea salir del programa? (S/N): ").upper()
            if confirmacion == 'S':
                guardar_datos_en_csv()  
                print("Saliendo del programa...")
                break
            else:
                print("Volviendo al menú principal...")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    conn.close()

menu_principal()
