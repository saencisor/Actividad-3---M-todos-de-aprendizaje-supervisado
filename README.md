# Actividad-3---M-todos-de-aprendizaje-supervisado
Sistema Inteligente de Rutas para Transporte Masivo
Descripción del Proyecto

Este proyecto fue desarrollado como parte de la asignatura de Inteligencia Artificial y tiene como objetivo implementar un sistema inteligente capaz de determinar rutas óptimas dentro de una red de transporte masivo utilizando el algoritmo de búsqueda heurística *A (A-Star)**.

El sistema modela una red de estaciones interconectadas, evalúa diferentes alternativas de recorrido y selecciona la ruta con menor costo considerando los tiempos de desplazamiento y las restricciones definidas, como estaciones cerradas por mantenimiento.

Adicionalmente, se construyó un conjunto de datos en formato CSV relacionado con variables de transporte (distancia, tiempo, costo y tipo de transporte), con el fin de proporcionar una base para futuros modelos de aprendizaje supervisado.

Objetivos
Implementar una base de conocimiento para representar una red de transporte masivo.
Aplicar reglas lógicas para gestionar restricciones operativas.
Utilizar una heurística para optimizar la búsqueda de rutas.
Implementar el algoritmo A* para encontrar caminos óptimos.
Generar y analizar un conjunto de datos relacionado con transporte masivo.
Tecnologías Utilizadas
Python
Pandas
NetworkX
Matplotlib
Heapq
Estructura del Proyecto
├── Ruta_Inteligente_3.py
├── transporte_masivo.csv
├── Informe_Final.pdf
├── Evidencias/
└── README.md
Dataset

El archivo transporte_masivo.csv contiene información de ejemplo relacionada con:

Distancia recorrida
Tiempo de viaje
Costo del desplazamiento
Medio de transporte utilizado

Este conjunto de datos fue creado con fines académicos para demostrar el uso de fuentes de datos en proyectos de Inteligencia Artificial.

Algoritmo Implementado

Se utilizó el algoritmo de búsqueda heurística A* (A-Star), el cual combina:


f(n) = g(n) + h(n)

Donde:

g(n): costo real acumulado desde el origen.
h(n): estimación heurística hasta el destino.
f(n): función de evaluación utilizada para priorizar la exploración de nodos.
Resultados

El sistema permite:

 Encontrar la mejor ruta entre dos estaciones.

 Calcular el tiempo estimado del recorrido.

 Gestionar estaciones bloqueadas por mantenimiento.

 Visualizar el mapa de la red de transporte.

 Generar y cargar un dataset de transporte masivo.

Ejemplo de Ejecución

Ingrese la estación inicial: A
Ingrese la estación destino: F
 
RUTA ÓPTIMA ENCONTRADA
 
A ➜ C ➜ D ➜ F
 
Tiempo total estimado: 12 minutos
Nodos explorados: 4
Cantidad de estaciones recorridas: 4

Autor

Shirly Alexandra Enciso Ruiz

Ingeniería de Software
