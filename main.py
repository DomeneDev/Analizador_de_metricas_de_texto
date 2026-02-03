"""
Fichero principal del programa
"""
from processador import limpiar_texto, contar_frecuencia, generar_metricas


def ejecutar_analizador():
    """
    Función principal del programa para ejecutar el analizado de texto
    """
    # Solicitar texto al usuario para analizarlo
    # Dentro de bucle While para validar dato de entrada
    while True:
        # Solicitamos texto
        texto = input("Introduce el texto a analizar:\n")
        # Verificamos que el texto es válido y no esta vacío o solo tiene espacios.
        try:
            if not texto.strip():
                raise ValueError(
                    "📛 No has introducido ningún texto o solo escribiste espacios.")
        except ValueError as e:
            print(f"❌ Error de validacion: \n\t-{e}")
        else:
            break
    # Limpiar texto
    texto_limpio = limpiar_texto(texto)
    # Cacular frecuencias
    frecuencia = contar_frecuencia(texto_limpio)
    # Generar las métricas
    metricas = generar_metricas(texto_limpio)
    # Mostra resultados
    print("+------------------------------------+")
    print("| Resultados del análisis del texto  |")
    print("+------------------------------------+")
    print(f" - Total de palabras del texto: {metricas['total_palabras']}.")
    print(f" - Palabra más larga: {metricas['palabra_mas_larga']}.")
    print(
        f" - Media de longitud de las palabras: {metricas['promedio_longitud']}.")
    print("- Cantidad de palabras:")
    for palabra, cantidad in frecuencia.items():
        if cantidad == 1:
            print(f" \t- {palabra}: {cantidad} vez")
        else:
            print(f" \t- {palabra}: {cantidad} veces.")


if __name__ == "__main__":
    ejecutar_analizador()
