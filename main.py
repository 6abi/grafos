
#imports necessarios
import pandas as pd
import networkx as nx
from matplotlib.pyplot import figure
import numpy as np


#leitura csv
file = "data.csv"
df = pd.read_csv(file, delimiter=";")
df = df.set_index("switch")
print(df)

#Lidando com NaN e "0"
df = df.replace(np.nan,0)
df = df.replace("0",0)
print(df)

#verifica conexão dos nós
df1 = df != 0
df1 = df1.reset_index()
df1 = df1.set_index("switch")

#%%
#colunas: fonte e alvos
source = df1.iloc[:,1:].columns
targets = df1.iloc[:,1:].columns

#%%
print(source)

#%%
print(targets)

#%%
#populando os nós
G =nx.from_pandas_adjacency(df1, create_using = nx.Graph())

#%%
print(nx.info(G))

#grafo
plt = figure(figsize=(12,12))
nx.draw_shell(G, with_labels=True, node_size=6000)
plt.show()