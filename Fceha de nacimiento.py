# Función 1: Validar que la cadena no esté vacía
def validar_no_vacio(cadena):
    return cadena.strip() != ""

# Función 2: Validar fecha de nacimiento (formato DD-MM-AAAA)
def validar_fecha(fecha):
    partes = fecha.split("-")
    
    # Validación manual del número de partes
    contador = 0
    for parte in partes:
        contador += 1
    if contador != 3:
        return False, "Formato inválido. Usa DD-MM-AAAA."
    
    dia, mes, año = partes

    # Validar que todos sean números
    if not (dia.isdigit() and mes.isdigit() and año.isdigit()):
        return False, "La fecha debe contener solo números y guiones."

    dia, mes, año = int(dia), int(mes), int(año)

    # Validar año mayor a 1900
    if año <= 1900:
        return False, "El año debe ser mayor a 1900."

    # Validar mes entre 1 y 12
    if mes < 1 or mes > 12:
        return False, "El mes debe estar entre 1 y 12."

    # Días por mes (sin bisiestos)
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):  # Año bisiesto
        dias_mes[1] = 29

    if dia < 1 or dia > dias_mes[mes - 1]:
        return False, f"El día {dia} no es válido para el mes {mes}."

    return True, "Fecha válida"

# Función 3: Verificar si ya cumplió años
def verificar_cumple(dia, mes, año):
    # Fecha actual fija (20/10/2025)
    dia_actual = 20
    mes_actual = 10
    año_actual = 2025

    edad = año_actual - año
    if (mes, dia) > (mes_actual, dia_actual):
        edad -= 1
        return edad, "Aún no ha cumplido años este año."
    else:
        return edad, "Ya cumplió años este año."

# Función principal
def main():
    # Solicitar la fecha de nacimiento al usuario
    fecha = input("Ingresa tu fecha de nacimiento (DD-MM-AAAA): ")

    # Validar que no esté vacía
    if not validar_no_vacio(fecha):
        print("Error: No puedes dejar la fecha vacía.")
        return

    # Validar fecha
    es_valida, mensaje = validar_fecha(fecha)
    if not es_valida:
        print("Error:", mensaje)
        return

    # Extraer valores para verificar cumpleaños
    dia, mes, año = map(int, fecha.split("-"))
    edad, mensaje_cumple = verificar_cumple(dia, mes, año)

    print("\no", mensaje)
    print(f"Tu edad es: {edad} años")
    print(mensaje_cumple)

# Llamada al programa
main()
