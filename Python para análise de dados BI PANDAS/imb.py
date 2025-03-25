import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


df = pd.read_csv('consulta.csv', sep=';', encoding='latin1')
df.columns = ['Ano', 'Município', 'População', 'PIB per Capita']
df['População'] = df['População'].str.replace('.','').astype(int)
df['PIB per Capita'] = df['PIB per Capita'].str.replace('.','').str.replace(',','.').astype(float)

df.dropna(inplace=True)


df_goiania = df[df['Município'] == 'Goiânia']
df_goiania = df_goiania.sort_values('Ano')

df_aragoiania = df[df['Município'] == 'Aragoiânia']
df_aragoiania = df_aragoiania.sort_values('Ano')
 
#Crescimento do PIB per capita (%) 
df_goiania['Crescimento PIB per Capita'] = df_goiania['PIB per Capita'].pct_change() * 100
df_aragoiania['Crescimento PIB per Capita'] = df_aragoiania['PIB per Capita'].pct_change() * 100

#Crescimento Populacional (%)
df_goiania['Crescimento Populacional'] = df_goiania['População'].pct_change() * 100
df_aragoiania['Crescimento Populacional'] = df_aragoiania['População'].pct_change() * 100

#Elasticidade do PIB per capita em relação à População
df_goiania['Elasticidade'] = df_goiania['Crescimento PIB per Capita'] / df_goiania['Crescimento Populacional']
df_aragoiania['Elasticidade'] = df_aragoiania['Crescimento PIB per Capita'] / df_aragoiania['Crescimento Populacional']


fig = plt.figure(figsize=(10, 6))
gs = GridSpec(2, 2, figure=fig)  


ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(df_goiania['Ano'], df_goiania['Crescimento PIB per Capita'])
ax1.plot(df_aragoiania['Ano'], df_aragoiania['Crescimento PIB per Capita'])
ax1.legend(['Goiânia', 'Aragoiânia'])
ax1.set_title('Crescimento PIB per Capita (%)')

ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(df_goiania['Ano'], df_goiania['Crescimento Populacional'])
ax2.plot(df_aragoiania['Ano'], df_aragoiania['Crescimento Populacional'])
ax2.legend(['Goiânia', 'Aragoiânia'])
ax2.set_title('Crescimento Populacional (%)')

ax3 = fig.add_subplot(gs[1, :])
ax3.plot(df_goiania['Ano'], df_goiania['Elasticidade'])
ax3.plot(df_aragoiania['Ano'], df_aragoiania['Elasticidade'])
ax3.legend(['Goiânia', 'Aragoiânia'])
ax3.set_title('Elasticidade (%)')

plt.show()