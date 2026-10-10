# ==========================================================
# ACTIVIDAD 3 - INTELIGENCIA ARTIFICIAL
# Sistema Inteligente de Rutas para Transporte Masivo
# Algoritmo A* (A-Star)
# ==========================================================

# Importar bibliotecas necesarias
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# ==========================================================
# CREACIÓN DEL DATASET
# ==========================================================

import pandas as pd

datos_transporte = {
    'distancia': [5, 3, 8, 2, 6, 4, 10, 1, 7, 3, 5, 9, 2, 4, 8, 1, 6, 3, 5, 7],
    'tiempo':    [15, 12, 25, 7, 18, 10, 30, 5, 20, 8, 14, 28, 6, 11, 23, 4, 17, 9, 13, 21],
    'costo':     [2500, 2000, 3000, 1500, 2500, 1800, 3500, 1200, 2800, 1700,
                  2200, 3400, 1300, 1900, 3100, 1000, 2600, 1600, 2100, 2900],
    'transporte': [
        'Bus', 'Tranvia', 'Bus', 'Metro', 'Bus',
        'Tranvia', 'Bus', 'Metro', 'Bus', 'Metro',
        'Tranvia', 'Bus', 'Metro', 'Tranvia', 'Bus',
        'Metro', 'Bus', 'Metro', 'Tranvia', 'Bus'
    ]
}

df = pd.DataFrame(datos_transporte)

# Exportar CSV
df.to_csv("transporte_masivo.csv", index=False)

print("Archivo transporte_masivo.csv generado correctamente.")
# ==========================================================
# CARGAR DATASET
# ==========================================================

datos = pd.read_csv("transporte_masivo.csv")

print("\nPrimeros registros del dataset:")
print(datos.head())
# ==========================================================
# 1. BASE DE CONOCIMIENTO
# Mapa de estaciones y tiempos de desplazamiento
# ==========================================================

conexiones = {
    'A': {'B': 9, 'C': 5},
    'B': {'A': 9, 'D': 2},
    'C': {'A': 5, 'D': 4},
    'D': {'B': 2, 'C': 4, 'F': 3, 'E': 6},
    'E': {'D': 6, 'F': 1},
    'F': {'D': 3, 'E': 1}
}


# ==========================================================
# 2. HEURÍSTICA
# Estimación aproximada del costo al destino
# ==========================================================

h = {
    'A': 10,
    'B': 0,
    'C': 7,
    'D': 2,
    'E': 8,
    'F': 5
}


# ==========================================================
# 3. REGLA LÓGICA
# Estaciones cerradas por mantenimiento
# ==========================================================

bloqueadas = ['E']


# ==========================================================
# 4. FUNCIÓN DE BÚSQUEDA A*
# ==========================================================

def buscar_camino(origen, destino):

    agenda = [(h[origen], 0, origen, [])]

    visitados = set()

    nodos_explorados = 0

    while agenda:

        f, g, nodo, camino = heapq.heappop(agenda)

        if nodo in visitados:
            continue

        # Regla lógica
        if nodo in bloqueadas:
            print(f"\n Estación {nodo} cerrada por mantenimiento")
            continue

        nodos_explorados += 1

        camino = camino + [nodo]

        if nodo == destino:
            return camino, g, nodos_explorados

        visitados.add(nodo)

        for vecino, peso in conexiones[nodo].items():

            if vecino not in visitados:

                nuevo_g = g + peso
                nuevo_f = nuevo_g + h[vecino]

                heapq.heappush(
                    agenda,
                    (nuevo_f, nuevo_g, vecino, camino)
                )

    return None, 0, nodos_explorados


# ==========================================================
# 5. VISUALIZACIÓN DEL MAPA
# ==========================================================

def mostrar_mapa():

    G = nx.Graph()

    for estacion, vecinos in conexiones.items():

        for vecino, peso in vecinos.items():
            G.add_edge(estacion, vecino, weight=peso)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        node_color='lightblue',
        font_size=12,
        font_weight='bold'
    )

    etiquetas = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=etiquetas
    )

    plt.title("Mapa de Transporte Masivo")
    plt.show()


# ==========================================================
# 6. SISTEMA EXPERTO DE RUTAS
# ==========================================================

print("=" * 50)
print(" SISTEMA INTELIGENTE DE RUTAS ")
print("=" * 50)

print("\nEstaciones disponibles:")
print(", ".join(conexiones.keys()))

origen = input("\nIngrese la estación inicial: ").upper()

destino = input("Ingrese la estación destino: ").upper()

if origen in conexiones and destino in conexiones:

    ruta, tiempo, explorados = buscar_camino(
        origen,
        destino
    )

    if ruta:

        print("\n RUTA ÓPTIMA ENCONTRADA")

        print("\nTrayectoria:")
        print(" ➜ ".join(ruta))

        print(f"\nTiempo total estimado: {tiempo} minutos")

        print(f"Nodos explorados: {explorados}")

        print(f"Cantidad de estaciones recorridas: {len(ruta)}")

        print("\nInterpretación:")
        print(
            "La ruta encontrada corresponde al "
            "camino con menor costo utilizando "
            "el algoritmo A*."
        )

    else:
        print("\n No existe una ruta disponible.")

else:
    print("\n Error: estación no registrada.")


# ==========================================================
# 7. MOSTRAR EL MAPA DEL SISTEMA
# ==========================================================

mostrar_mapa()