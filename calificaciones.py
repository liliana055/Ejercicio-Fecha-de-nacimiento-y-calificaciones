# Función 1: Validar que los datos no estén vacíos
def validar_datos(datos):
    # Verificamos que ninguno de los datos esté vacío
    for dato in datos:
        if not dato.strip():
            return False
    return True

# Función 2: Evaluar si un alumno aprobó o reprobó
def evaluar_alumno(calificaciones):
    # Lista para almacenar los resultados de evaluación
    resultados = []
    
    # Evaluar cada calificación
    for calificacion in calificaciones:
        if calificacion > 6:
            resultados.append("Aprobado")
        else:
            resultados.append("Reprobado")
    
    return resultados

# Función 3: Procesar los datos de un alumno (nombre, matrícula y calificaciones)
def procesar_alumno(datos, index, num_materias):
    # Extraer el nombre y matrícula del alumno
    nombre_alumno = datos[index].strip()
    matricula = datos[index + 1].strip()
    
    # Validar que el nombre y matrícula no estén vacíos
    if not validar_datos([nombre_alumno, matricula]):
        print("Error: El nombre y matrícula no pueden estar vacíos.")
        return None, index

    # Extraer las calificaciones del alumno
    calificaciones = []
    for i in range(num_materias):
        try:
            # Obtener la calificación de la materia
            calificacion = float(datos[index + 2 + i].strip())
            if 0 <= calificacion <= 10:
                calificaciones.append(calificacion)
            else:
                print(f"Error: La calificación de la materia {i+1} debe estar entre 0 y 10.")
                return None, index
        except ValueError:
            print(f"Error: La calificación de la materia {i+1} debe ser un número válido.")
            return None, index

    return (nombre_alumno, matricula, calificaciones), index + 2 + num_materias

# Función principal
def main():
    # Pedir todos los datos en un solo input
    datos_input = input("Ingresa el número de alumnos, número de materias, y luego por cada alumno: nombre, matrícula y calificaciones separadas por comas. Ejemplo: 3,2,Juan Pérez,12345,8,7,8,  .... : ")
    
    # Separar la entrada en una lista de datos
    datos = datos_input.split(",")
    
    # Mostrar los datos procesados (para depuración)
    print("\nDatos procesados:")
    print(datos)
    
    # Validar los datos (Asegurarse de que la entrada no esté vacía)
    if not validar_datos(datos):
        print("Error: Ningún campo puede estar vacío.")
        return
    
    # Extraer el número de alumnos y materias
    num_alumnos = int(datos[0].strip())
    num_materias = int(datos[1].strip())
    
    # Contador de índice en la lista para procesar cada alumno
    index = 2  # Empieza después del número de alumnos y materias
    
    # Procesar cada alumno
    for alumno in range(1, num_alumnos + 1):
        print(f"\n--- Alumno {alumno} ---")
        
        # Procesar los datos del alumno
        alumno_info, index = procesar_alumno(datos, index, num_materias)
        
        if alumno_info is None:
            return  # Si hubo un error, no continuar con más alumnos
        
        nombre_alumno, matricula, calificaciones = alumno_info
        
        print(f"\nEvaluando al alumno: {nombre_alumno}, Matrícula: {matricula}")
        
        # Evaluar las calificaciones
        resultados = evaluar_alumno(calificaciones)
        
        # Mostrar resultados
        for i, resultado in enumerate(resultados):
            print(f"Materia {i + 1}: {resultado}")
    
# Llamada al programa principal
main()
