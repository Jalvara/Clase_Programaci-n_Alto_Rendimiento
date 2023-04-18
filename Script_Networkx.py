import networkx as nx
import json
import matplotlib.pyplot as plt
import pygraphviz as pgv

def ImprimirGrafo(G,colors):
    fig, ax=plt.subplots(1,1,figsize=(14,10))
    pos=nx.drawing.nx_agraph.graphviz_layout(G,prog='neato')
    nx.draw(G,pos,ax=ax,node_size=200,node_color=colors)
    nx.draw_networkx_labels(G,pos=pos,ax=ax,font_size=6)
    #nx.draw_networkx_edges(g,pos=pos,ax=ax,edgelist=LT,width=2)
    #nx.draw_networkx_edges(g,pos=pos,ax=ax,edgelist=LP,edge_color="blue")
    #ax.set_title("Conecciones del metro")
    plt.show()
#Esta funcion dibujara un subgrafo resaltando sus aristas para la visualizacion rapida del 
#subgrafo.    
def ImprimirSubgrafo(G,G1,colors,colors1):
    fig, ax=plt.subplots(1,1,figsize=(14,10))
    pos=nx.drawing.nx_agraph.graphviz_layout(G,prog='neato')
    nx.draw(G,pos,ax=ax,node_size=200,node_color=colors)
    nx.draw(G1,pos,ax=ax,node_size=200,node_color=colors1)
    nx.draw_networkx_labels(G,pos=pos,ax=ax,font_size=6)
    #nx.draw_networkx_edges(G,pos=pos,ax=ax,edgelist=G1.edges(),width=4)
    nx.draw_networkx_edges(G,pos=pos,ax=ax,edgelist=G1.edges(),edge_color="red")
    #ax.set_title("Conecciones del metro")
    plt.show()
def ImprimirSubgrafos(G,N):
    # Obtener el camino más corto desde el nodo N a todos los demás nodos en el grafo G
    caminos_cortos = nx.single_source_shortest_path(G, N)
    # Imprimir los caminos más cortos
    LG=[]
    for nodo, camino in caminos_cortos.items():
        l=[(camino[k],camino[k+1]) for k in range(len(camino)-1)]
        g1=nx.DiGraph()
        g1.add_edges_from(l)
        LG.append(g1)
    fig, ax=plt.subplots(1,1,figsize=(14,10))
    pos=nx.drawing.nx_agraph.graphviz_layout(G,prog='neato')
    for grafo in LG:
        nx.draw_networkx_edges(G,pos=pos,ax=ax,edgelist=grafo.edges(),edge_color="red",width=5)
        nx.draw(grafo,pos,ax=ax,node_size=200)
    nx.draw(G,pos,ax=ax,node_size=200,node_color=colors)
    nx.draw_networkx_labels(G,pos=pos,ax=ax,font_size=6)
    plt.show()
#Cargar la informacion del archivos json
with open("tokyo-metro.json") as f:
    data=json.load(f)
print("------Impriendo las llaves de data--------")
print(data.keys())
#print("------Impriendo los valores de data--------")
#print(data.values())
#print("Informacion de la linea  C: ")
#print(data['C'])
#Construcción del grafo usando la informacion de data
g=nx.Graph()
#Construir los nodos y las aristas del grafo, donde cada nodo
# es una estación de alguna de las líneas del metro. 
for line in data.values():
    g.add_weighted_edges_from(line["travel_times"])
    g.add_edges_from(line["transfers"])
#Podemos consultar si un atributo es parte de una arista mediante
#la siguiente instruccion:
#print("Contenido de g['Z10']['Z11']: ",g['Z10']['Z11'])
#print('weight' in g['Z10']['Z11'])   
#print("Contenido de g['C8']['M15']: ",g['C8']['M15'])
#print('weight' in g['C8']['M15'])
for a,b in g.edges():
    g[a][b]['transfer']='weight' in g[a][b]
#funcion con la que se puede obtener la data de una arista:
print(g.get_edge_data('Z10','Z11')) 
x=('Z10','Z11') 
print(g.get_edge_data(*x))  
LP=[e for e in g.edges() if g.get_edge_data(*e)['transfer']]
LT=[e for e in g.edges() if not g.get_edge_data(*e)['transfer']] 
#Creando la lista de colores correspondientes a cada nodo. 
colors=[data[n[0].upper()]['color'] for n in g.nodes()]
#print(colors)
#Parte de la visualizacion del grafo:
#ImprimirGrafo(g,colors)
print("Numero de nodos: ",g.number_of_edges())
print("Numero de aristas: ",g.number_of_nodes())
print("Nodos adyacentes de",'C12',list(g.neighbors('C12')))
#Determinando si g contiene un camino especifico:
print("Existe un camino entre M19, C12 y M19?: ",nx.is_path(g,['M19','C12','C13']))
#Determinando el peso de un camino especifico:
Camino=['C'+str(k) for k in range(1,13)]
print(Camino)
print("Peso del camino C1 a C12: ", nx.path_weight(g,Camino,'weight'))
#Problema del camino mas corto desde una o mas fuentes. 
g1=nx.shortest_path(g,'C1','M21','weight')
print('Camino encontrado: ',g1)
l1=[(g1[k],g1[k+1]) for k in range(len(g1)-1)]
g1=nx.DiGraph()
g1.add_edges_from(l1)
print('Aristas del nuevo grafo: ',g1.edges())
colors1=[data[n[0].upper()]['color'] for n in g1.nodes()]
#ImprimirGrafo(g1,colors1)
#ImprimirSubgrafo(g,g1,colors,colors1)
#Calculando todos los caminos simples desde un nodo
#g1=nx.single_source_shortest_path(g,'C1')
#print(g1)
#Ejercicio: Crear la funcion:
# def ImprimirSubgrafos(G,N):
#Esta funcion debe imprimir los caminos mas cortos desde el nodo N hasta el resto de 
#nodos del grafo. 
ImprimirSubgrafos(g,'C1')