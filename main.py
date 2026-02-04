"""
Fichero principal del programa
"""
from processador import limpiar_texto, contar_frecuencia, generar_metricas
from utils import leer_texto, mostrar_resultados

# ---- CONSTANTES DE CONFIGURACIÓN ----
PROMPT_ANALISIS = "Introduce el texto a analizar:\n"
ERR_TEXTO_VACIO = "🛑 El texto está vacio"


def ejecutar_analizador():
    """
    Función principal del programa para ejecutar el analizado de texto
    """
    # Solicitar texto al usuario para analizarlo
    texto = leer_texto(PROMPT_ANALISIS, ERR_TEXTO_VACIO)
    # Limpiar texto
    texto_limpio = limpiar_texto(texto)
    # Cacular frecuencias
    frecuencia = contar_frecuencia(texto_limpio)
    # Generar las métricas
    metricas = generar_metricas(texto_limpio)
    # Mostra resultados
    mostrar_resultados(metricas, frecuencia)


if __name__ == "__main__":
    ejecutar_analizador()
