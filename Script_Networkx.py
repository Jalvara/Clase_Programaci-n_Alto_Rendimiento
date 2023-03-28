import networkx as nx
import json
import matplotlib.pyplot as plt
import pygraphviz as pgv

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
fig, ax=plt.subplots(1,1,figsize=(14,10))
pos=nx.drawing.nx_agraph.graphviz_layout(g,prog='neato')
nx.draw(g,pos,ax=ax,node_size=200,node_color=colors)
nx.draw_networkx_labels(g,pos=pos,ax=ax,font_size=6)
nx.draw_networkx_edges(g,pos=pos,ax=ax,edgelist=LT,width=2)
nx.draw_networkx_edges(g,pos=pos,ax=ax,edgelist=LP,edge_color="blue")
ax.set_title("Conecciones del metro")
plt.show()