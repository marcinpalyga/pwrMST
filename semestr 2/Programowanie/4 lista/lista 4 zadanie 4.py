import os
import matplotlib.pyplot as plt
import imageio
import networkx as nx
import random
G = nx.fast_gnp_random_graph(20, 0.5)
nx.draw(G, with_labels = True)
plt.show()

position = nx.spring_layout(G, seed=100)    
neigh_list = [1]   
filenames = []
for i in range(20):
    color_map = ['#000000'] * 20    
    color_map[random.choice(neigh_list)] = '#ff0000'    
    nx.draw(G, pos=position, node_color=color_map)

    neigh_list = []
    for f in G.neighbors(color_map.index('#ff0000')):
        neigh_list.append(int(f))

    filename = f'{i}.png'     
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()

with imageio.get_writer('Walk.gif', mode='I', fps=2) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

for filename in filenames:
    os.remove(filename)
