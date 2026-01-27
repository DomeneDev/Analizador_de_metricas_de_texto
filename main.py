from processador import limpiar_texto, contar_frecuencia, generar_metricas


def ejecutar_analizador():
    # Solicitar texto al usuario para analizarlo
    texto = input("Introduce el texto a analizar:\n")
    
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
    print(f" - Media de longitud de las palabras: {metricas['promedio_longitud']}.")
    print("- Cantidad de palabras:")
    for palabra, cantidad in frecuencia.items():
        if cantidad == 1:
            print(f" \t- {palabra}: {cantidad} vez")
        else:
            print(f" \t- {palabra}: {cantidad} veces.")

if __name__ == "__main__":
    ejecutar_analizador()