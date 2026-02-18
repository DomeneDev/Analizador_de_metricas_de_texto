"""
Fichero principal del programa
"""
from processador import limpiar_texto, contar_frecuencia, generar_metricas, preparar_registro
from utils import leer_texto, mostrar_resultados
from storage_manager import cargar_json, guardar_json


# ---- CONSTANTES DE CONFIGURACIÓN ----
PROMPT_ANALISIS = "Introduce el texto a analizar:\n"
ERR_TEXTO_VACIO = "🛑 El texto está vacio"

# --- CONSTANTES DE IMPUTS ---
INPUT_CONFIRMAR_GUARDADO = "Desea guardar el analisis realizado en el historial (S/N): "

# --- CONSTANTES DE OUTPUT ---
OUTPUT_CONFIRMADO_GUARDADO = "✅ Registro guardado en fichero de historial: "
OUTPUT_CANCELADO_GUARDADO = "✅ Cancealdo el guardado del registro actual."
OUTPUT_ERROR_DATO = "🛑 Debe introducir un dato válido."

# ---- CONSTANTE RUTA ARCHIVO JSON ---
RUTA = "analizador_texto/data/historial_analisis.json"


def ejecutar_analizador():
    """
    Función principal del programa para ejecutar el analizado de texto
    """
    # Cargar fichero de historial de analizador
    historial = cargar_json(RUTA)
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
    # Confirmación de guardado del analisis realizado.
    while True:
        try:
            opcion = input(INPUT_CONFIRMAR_GUARDADO).upper()
            match opcion:
                case "S":
                    registro = preparar_registro(texto, metricas)
                    historial.append(registro)
                    guardar_json(historial, RUTA)
                    print(OUTPUT_CONFIRMADO_GUARDADO)
                    break
                case "N":
                    print(OUTPUT_CANCELADO_GUARDADO)
                    break
                case _:
                    print(OUTPUT_ERROR_DATO)
        except ValueError:
            print(OUTPUT_ERROR_DATO)


if __name__ == "__main__":
    ejecutar_analizador()
