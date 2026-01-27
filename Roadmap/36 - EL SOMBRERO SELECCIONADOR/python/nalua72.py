import random
import time
"""
/*
 * EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
 */
"""

HOUSES = ["mobile", "frontend", "data", "backend"]


def main():

    houses = {house: 0 for house in HOUSES}

    questions = [
        {
            "question": "¿Qué tipo de proyectos te interesa más desarrollar?",
            "answers": [
                {
                    "option": "Aplicaciones móviles nativas para múltiples plataformas.",
                    "house": "Mobile"
                },
                {
                    "option": "Interfaces visualmente atractivas y responsivas.",
                    "house": "Frontend"
                },
                {
                    "option": "Procesamiento y análisis de grandes volúmenes de datos.",
                    "house": "Data"
                },
                {
                    "option": "Sistemas robustos y optimización de rendimiento del servidor.",
                    "house": "Backend"
                }
            ]
        },
        {
            "question": "¿Qué aspecto del desarrollo disfrutas más?",
            "answers": [
                {
                    "option": "Resolver problemas complejos de lógica y escalabilidad.",
                    "house": "Backend"
                },
                {
                    "option": "Analizar datos para tomar decisiones basadas en estadísticas.",
                    "house": "Data"
                },
                {
                    "option": "Crear aplicaciones móviles eficientes y funcionales.",
                    "house": "Mobile"
                },
                {
                    "option": "Trabajar en el diseño y la experiencia de usuario.",
                    "house": "Frontend"
                }
            ]
        },
        {
            "question": "¿Qué herramienta prefieres usar en tu día a día?",
            "answers": [
                {
                    "option": "Kotlin o Swift para desarrollar apps móviles nativas.",
                    "house": "Mobile"
                },
                {
                    "option": "Python o R para análisis de datos.",
                    "house": "Data"
                },
                {
                    "option": "Frameworks como React o Angular.",
                    "house": "Frontend"
                },
                {
                    "option": "Lenguajes como Node.js o Python para la gestión de servidores.",
                    "house": "Backend"
                }
            ]
        },
        {
            "question": "¿Cómo te ves en un equipo de desarrollo?",
            "answers": [
                {
                    "option": "Modelando datos y construyendo dashboards de análisis.",
                    "house": "Data"
                },
                {
                    "option": "Encargado de la lógica del servidor y las APIs.",
                    "house": "Backend"
                },
                {
                    "option": "Desarrollando la interfaz y funcionalidad de una app móvil.",
                    "house": "Mobile"
                },
                {
                    "option": "Diseñando las interacciones y los componentes visuales.",
                    "house": "Frontend"
                }
            ]
        },
        {
            "question": "¿Qué te motiva más al trabajar en un proyecto?",
            "answers": [
                {
                    "option": "Ver cómo el diseño cobra vida en la pantalla.",
                    "house": "Frontend"
                },
                {
                    "option": "Descubrir insights a partir del análisis de datos.",
                    "house": "Data"
                },
                {
                    "option": "Optimizar el rendimiento y escalabilidad del sistema.",
                    "house": "Backend"
                },
                {
                    "option": "Lograr que una aplicación móvil funcione perfectamente en cualquier dispositivo.",
                    "house": "Mobile"
                }
            ]
        },
        {
            "question": "¿Cuál es tu enfoque al aprender nuevas tecnologías?",
            "answers": [
                {
                    "option": "Explorar técnicas avanzadas de análisis de datos y machine learning.",
                    "house": "Data"
                },
                {
                    "option": "Aprender sobre nuevas arquitecturas y lenguajes de servidor.",
                    "house": "Backend"
                },
                {
                    "option": "Probar nuevas plataformas y herramientas para desarrollo móvil.",
                    "house": "Mobile"
                },
                {
                    "option": "Experimentar con nuevas librerías y frameworks de interfaz de usuario.",
                    "house": "Frontend"
                }
            ]
        },
        {
            "question": "¿Qué tipo de desafíos disfrutas más resolver?",
            "answers": [
                {
                    "option": "Solución de problemas de concurrencia y carga en servidores.",
                    "house": "Backend"
                },
                {
                    "option": "Optimización de interfaces para que se vean bien en cualquier dispositivo.",
                    "house": "Frontend"
                },
                {
                    "option": "Análisis de grandes volúmenes de datos para detectar patrones ocultos.",
                    "house": "Data"},
                {
                    "option": "Creación de experiencias de usuario fluídas en dispositivos móviles.",
                    "house": "Mobile"
                }
            ]
        },
        {
            "question": "¿Cómo te gusta medir el éxito de tu trabajo?",
            "answers": [
                {
                    "option": "Por la estabilidad y rapidez del sistema bajo carga.",
                    "house": "Backend"
                },
                {
                    "option": "Mediante la satisfacción del usuario con la interfaz visual.",
                    "house": "Frontend"
                },
                {
                    "option": "Por la fluidez y buen rendimiento de la app móvil en diferentes dispositivos.",
                    "house": "Mobile"},
                {
                    "option": "Por la precisión y relevancia de los resultados obtenidos en el análisis de datos.",
                    "house": "Data"
                }
            ]
        },
        {
            "question": "¿Qué te resulta más interesante al trabajar con tecnologías emergentes?",
            "answers": [
                {
                    "option": "Trabajar con tecnologías de big data o inteligencia artificial.",
                    "house": "Data"
                },
                {
                    "option": "Explorar nuevas arquitecturas para mejorar el rendimiento del servidor.",
                    "house": "Backend"
                },
                {
                    "option": "Probar nuevas herramientas y metodologías para mejorar el diseño y la UX.",
                    "house": "Frontend"
                },
                {
                    "option": "Desarrollar apps móviles que aprovechen nuevas capacidades de hardware.",
                    "house": "Mobile"
                }
            ]
        },
        {
            "question": "¿Cómo te enfrentas a un nuevo problema en un proyecto?",
            "answers": [
                {
                    "option": "Buscando patrones y soluciones basadas en análisis de datos.",
                    "house": "Data"
                },
                {
                    "option": "Replanteando la estructura visual y funcional de la interfaz.",
                    "house": "Frontend"
                },
                {
                    "option": "Explorando cómo mejorar la experiencia del usuario en dispositivos móviles.",
                    "house": "Mobile"
                },
                {
                    "option": "Analizando la estructura de datos y la lógica del backend.",
                    "house": "Backend"
                }
            ]
        }
    ]

    print("Director: Bienvenido a la escuela Howarts para magos y brujas del código")
    print("Director: Como bien sabéis, la escuela tiene 4 casas, a saber: Frontend, Backend, Mobile y Data.")
    print("Director: Para saber a que casa os unireis cada uno, os pondremos al sombrero seleccionador que os hará unas preguntas y al finalizar os dirá a que casa deberéis incorporaros.")
    print("Director: A ver, que suba el primero")
    alumno = input("Sombrero: ¿Cómo te llamas muchado?: ")

    print(
        f"Sombrero: Muy bien {alumno}, te voy a hacer 10 preguntas y tienes que escoger entre cuatro posibles respuestas. ¿Listo?")
    print(f"{alumno}: Sí señor")

    print("Sombrero: Vamos allá:\n")

    for question in questions:
        print(question["question"])
        for i, answer in enumerate(question["answers"], start=1):
            print(f"\t{i} - {answer['option']}")

        while True:
            try:
                opcion = int(input("Escoge una opción (1-4): "))
                if 1 <= opcion <= 4:
                    break
                print("⚠️ Debes elegir un número entre 1 y 4")
            except ValueError:
                print("⚠️ Introduce un número válido")

        house = question["answers"][opcion - 1]["house"]
        houses[house.lower()] += 1
        print()

    max_score = max(houses.values())
    winners = [house for house, score in houses.items() if score == max_score]

    if len(winners) > 1:
        print("Sombrero: Ummmm... esta decisión no es nada fácil...")
        time.sleep(2)
        final_house = random.choice(winners)
    else:
        final_house = winners[0]

    print(f"\n🎉 {alumno}, tu casa será: {final_house.capitalize()}!")


if __name__ == "__main__":
    main()
