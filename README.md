Analizador de Métricas de Texto
Este es un proyecto modular en Python diseñado para procesar cadenas de texto y extraer métricas estadísticas de contenido. El proyecto está enfocado en aplicar buenas prácticas de desarrollo, tipado estático y modularización de código.

🚀 Características
Limpieza de Datos: Normalización de texto (minúsculas y eliminación de puntuación).

Frecuencia de Palabras: Generación de diccionarios con el conteo de cada término.

Estadísticas Avanzadas: \* Conteo total de palabras.

Identificación de la palabra más larga.

Cálculo de la longitud promedio de las palabras.

📂 Estructura del Proyecto
La arquitectura del código sigue el principio de separación de responsabilidades:

Plaintext

analizador_texto/

├── main.py # Interfaz de usuario y orquestación del programa.

├── procesador.py # Núcleo lógico (motor de procesamiento).

└── README.md # Documentación del proyecto.

🛠️ Instalación y Uso
Clona este repositorio o descarga los archivos.

Asegúrate de tener instalado Python 3.9 o superior.

Ejecuta el programa principal:

Bash

python main.py
📝 Ejemplo de Salida
Plaintext

Introduce el texto a analizar: Python es genial, y programar en Python es divertido.

Frecuencia de palabras: {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'programar': 1, 'en': 1, 'divertido': 1}
Estadísticas: {
'total_palabras': 8,
'palabra_mas_larga': 'programar',
'promedio_longitud': 5.25
}
🛡️ Roadmap de Aprendizaje
Este proyecto evolucionará conforme avance mi formación en Python:

[x] Sprint 1: Lógica core y modularización (Estado actual).

[ ] Sprint 2: Implementación de manejo de excepciones (try-except).

[ ] Sprint 3: Persistencia de datos en archivos .json y .csv.

[ ] Sprint 4: Refactorización a Programación Orientada a Objetos (POO).
