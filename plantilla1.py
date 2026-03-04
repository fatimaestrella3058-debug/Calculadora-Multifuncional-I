"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:
- Estudiante 1: [Fatima] - Estructura Principal y Gestión de Datos
- Estudiante 2: [Ricardo] - Funciones Matemáticas
- Estudiante 3: [Raul]- Conversores y Sistema de Historial

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

import os
from datetime import datetime

# Variable global para almacenar historial (lista de strings)
historial = []

# ============================================
# SECCIÓN 1: FUNCIONES MATEMÁTICAS (Estudiante 2)
# ============================================

def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la suma
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Minuendo
        b (float): Sustraendo

    Returns:
        float: Resultado de la resta
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la multiplicación
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números validando división por cero.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Resultado de la división
        None: Si el divisor es cero
    """
    if b == 0:
        return None
    else:
        return a / b


def modulo(a, b):
    """
    Calcula el módulo entre dos números.

    Args:
        a (float): Número
        b (float): Divisor

    Returns:
        float: Residuo de la división
    """
    return a % b


def potencia(a, b):
    """
    Eleva un número a la potencia de otro.

    Args:
        a (float): Base
        b (float): Exponente

    Returns:
        float: Resultado de la potencia
    """
    return a ** b


# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS
# ============================================

def decimal_a_binario(numero):
    """
    Convierte un número decimal a binario utilizando división sucesiva.

    Args:
        numero (int): Número decimal

    Returns:
        str: Número convertido a binario
    """
    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        residuo = numero % 2
        resultado = str(residuo) + resultado
        numero = numero // 2

    return resultado


def decimal_a_hexadecimal(numero):
    """
    Convierte un número decimal a hexadecimal manualmente.

    Args:
        numero (int): Número decimal

    Returns:
        str: Número convertido a hexadecimal
    """
    if numero == 0:
        return "0"

    caracteres = "0123456789ABCDEF"
    resultado = ""

    while numero > 0:
        residuo = numero % 16
        resultado = caracteres[residuo] + resultado
        numero = numero // 16

    return resultado


def binario_a_decimal(binario):
    """
    Convierte un número binario a decimal.

    Args:
        binario (str): Número en formato binario

    Returns:
        int: Número convertido a decimal
    """
    decimal = 0
    potencia = 0

    for digito in reversed(binario):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1

    return decimal


def hexadecimal_a_decimal(hexadecimal):
    """
    Convierte un número hexadecimal a decimal.

    Args:
        hexadecimal (str): Número en formato hexadecimal

    Returns:
        int: Número convertido a decimal
    """
    caracteres = "0123456789ABCDEF"
    decimal = 0
    potencia = 0

    for digito in reversed(hexadecimal.upper()):
        valor = caracteres.index(digito)
        decimal += valor * (16 ** potencia)
        potencia += 1

    return decimal


# ============================================
# SECCIÓN 3: CONVERSIÓN DE UNIDADES
# ============================================

def bytes_a_kilobytes(bytes_val):
    """
    Convierte Bytes a Kilobytes.

    Args:
        bytes_val (float): Cantidad en bytes

    Returns:
        float: Equivalente en kilobytes
    """
    return bytes_val / 1024


def kilobytes_a_megabytes(kb):
    """
    Convierte Kilobytes a Megabytes.
    """
    return kb / 1024


def megabytes_a_gigabytes(mb):
    """
    Convierte Megabytes a Gigabytes.
    """
    return mb / 1024


def gigabytes_a_megabytes(gb):
    """
    Convierte Gigabytes a Megabytes.
    """
    return gb * 1024


def megabytes_a_kilobytes(mb):
    """
    Convierte Megabytes a Kilobytes.
    """
    return mb * 1024


def kilobytes_a_bytes(kb):
    """
    Convierte Kilobytes a Bytes.
    """
    return kb * 1024


# ============================================
# SECCIÓN 4: GESTIÓN DE HISTORIAL
# ============================================

def agregar_al_historial(operacion, num1, num2, resultado):
    """
    Agrega una operación al historial (máximo 10 registros).

    Args:
        operacion (str): Nombre de la operación realizada
        num1 (float): Primer número
        num2 (float): Segundo número
        resultado (float): Resultado obtenido
    """
    global historial

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = f"{fecha_hora} | {operacion}: {num1}, {num2} = {resultado}"
    historial.append(entrada)

    if len(historial) > 10:
        historial.pop(0)


def mostrar_historial():
    """
    Muestra en pantalla el historial de operaciones guardadas.
    """
    global historial

    if not historial:
        print("Historial vacío.")
    else:
        for i, operacion in enumerate(historial, 1):
            print(f"{i}. {operacion}")


def limpiar_historial():
    """
    Elimina todas las operaciones almacenadas en el historial.
    """
    global historial
    historial.clear()


# ============================================
# SECCIÓN 5: GESTIÓN DE ARCHIVOS
# ============================================

def guardar_historial_archivo():
    """
    Guarda el historial en el archivo datos/historial.txt.
    """
    global historial

    if not os.path.exists("datos"):
        os.makedirs("datos")

    with open("datos/historial.txt", "w") as archivo:
        for linea in historial:
            archivo.write(linea + "\n")


def cargar_historial_archivo():
    """
    Carga el historial desde el archivo si existe.
    """
    global historial

    if os.path.exists("datos/historial.txt"):
        with open("datos/historial.txt", "r") as archivo:
            for linea in archivo:
                historial.append(linea.strip())


# ============================================
# SECCIÓN 6: VALIDACIÓN
# ============================================

def validar_numero(mensaje):
    """
    Solicita un número decimal validando la entrada.

    Args:
        mensaje (str): Texto mostrado al usuario

    Returns:
        float: Número válido ingresado
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingrese un número válido.")


def validar_numero_entero(mensaje):
    """
    Solicita un número entero validando la entrada.

    Args:
        mensaje (str): Texto mostrado al usuario

    Returns:
        int: Número entero válido
    """
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingrese un número entero válido.")


# ============================================
# SECCIÓN 7: MENÚS
# ============================================

def mostrar_menu_principal():
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "="*60)
    print("   CALCULADORA MULTIFUNCIONAL v2.0")
    print("="*60)
    print("\nMENÚ PRINCIPAL:")
    print("1. Calculadora Básica")
    print("2. Conversor de Unidades de Datos")
    print("3. Calculadora de Sistemas Numéricos")
    print("4. Ver Historial")
    print("5. Limpiar Historial")
    print("6. Salir")
    print("-"*60)


def menu_calculadora_basica():
    """
    Muestra el submenú de operaciones matemáticas básicas.
    """
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Potencia")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione operación: ")

    if opcion == "7":
        return

    num1 = validar_numero("Ingrese el primer número: ")
    num2 = validar_numero("Ingrese el segundo número: ")

    if opcion == "1":
        resultado = sumar(num1, num2)
        print("Resultado:", resultado)
        agregar_al_historial("Suma", num1, num2, resultado)

    elif opcion == "2":
        resultado = restar(num1, num2)
        print("Resultado:", resultado)
        agregar_al_historial("Resta", num1, num2, resultado)

    elif opcion == "3":
        resultado = multiplicar(num1, num2)
        print("Resultado:", resultado)
        agregar_al_historial("Multiplicación", num1, num2, resultado)

    elif opcion == "4":
        resultado = dividir(num1, num2)
        if resultado is None:
            print("Error: No se puede dividir entre cero.")
        else:
            print("Resultado:", resultado)
            agregar_al_historial("División", num1, num2, resultado)

    elif opcion == "5":
        resultado = modulo(num1, num2)
        print("Resultado:", resultado)
        agregar_al_historial("Módulo", num1, num2, resultado)

    elif opcion == "6":
        resultado = potencia(num1, num2)
        print("Resultado:", resultado)
        agregar_al_historial("Potencia", num1, num2, resultado)

    else:
        print("Opción inválida.")


def menu_conversor_unidades():
    """
    Muestra el submenú de conversión de unidades de almacenamiento.
    """
    print("\n--- CONVERSOR DE UNIDADES ---")
    print("1. Bytes a Kilobytes")
    print("2. Kilobytes a Megabytes")
    print("3. Megabytes a Gigabytes")
    print("4. Gigabytes a Megabytes")
    print("5. Megabytes a Kilobytes")
    print("6. Kilobytes a Bytes")
    print("7. Volver")

    opcion = input("Seleccione opción: ")

    if opcion == "7":
        return

    valor = validar_numero("Ingrese el valor: ")

    if opcion == "1":
        print("Resultado:", bytes_a_kilobytes(valor))
    elif opcion == "2":
        print("Resultado:", kilobytes_a_megabytes(valor))
    elif opcion == "3":
        print("Resultado:", megabytes_a_gigabytes(valor))
    elif opcion == "4":
        print("Resultado:", gigabytes_a_megabytes(valor))
    elif opcion == "5":
        print("Resultado:", megabytes_a_kilobytes(valor))
    elif opcion == "6":
        print("Resultado:", kilobytes_a_bytes(valor))
    else:
        print("Opción inválida.")


def menu_sistemas_numericos():
    """
    Muestra el submenú de conversión entre sistemas numéricos.
    """
    print("\n--- SISTEMAS NUMÉRICOS ---")
    print("1. Decimal a Binario")
    print("2. Decimal a Hexadecimal")
    print("3. Binario a Decimal")
    print("4. Hexadecimal a Decimal")
    print("5. Volver")

    opcion = input("Seleccione opción: ")

    if opcion == "5":
        return

    if opcion == "1":
        numero = validar_numero_entero("Ingrese número decimal: ")
        print("Resultado:", decimal_a_binario(numero))

    elif opcion == "2":
        numero = validar_numero_entero("Ingrese número decimal: ")
        print("Resultado:", decimal_a_hexadecimal(numero))

    elif opcion == "3":
        binario = input("Ingrese número binario: ")
        print("Resultado:", binario_a_decimal(binario))

    elif opcion == "4":
        hexadecimal = input("Ingrese número hexadecimal: ")
        print("Resultado:", hexadecimal_a_decimal(hexadecimal))

    else:
        print("Opción inválida.")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """
    Función principal que ejecuta el programa y controla el menú interactivo.
    """
    print("╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  CALCULADORA MULTIFUNCIONAL - Versión Avanzada".center(58) + "║")
    print("║" + " "*58 + "║")
    print("║" + "  Con historial, funciones y persistencia de datos".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")

    cargar_historial_archivo()
    print("\nHistorial cargado desde archivo.")

    continuar = True

    while continuar:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_calculadora_basica()

        elif opcion == "2":
            menu_conversor_unidades()

        elif opcion == "3":
            menu_sistemas_numericos()

        elif opcion == "4":
            mostrar_historial()

        elif opcion == "5":
            confirmacion = input("\n¿Está seguro de limpiar el historial? (s/n): ")
            if confirmacion.lower() == "s":
                limpiar_historial()
                print("Historial limpiado.")

        elif opcion == "6":
            print("\nGuardando historial...")
            guardar_historial_archivo()
            print("Historial guardado en datos/historial.txt")
            print("\nGracias por usar la Calculadora Multifuncional.")
            continuar = False

        else:
            print("\nOpción inválida. Seleccione 1-6.")

    print("\nPrograma terminado.")


if __name__ == "__main__":
    main()
