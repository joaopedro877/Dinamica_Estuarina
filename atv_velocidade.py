# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:24:51 2023

@author: jdebr
"""

import numpy as np
import math
import matplotlib.pyplot as plt

#abrindo o arquivo em .mat
#https://www.askpython.com/python/examples/mat-files-in-python
from scipy.io import loadmat
annots = loadmat('C:/Users/jdebr/Documents/Oceanografia/Disciplinas/Dinâmica Estuarina/Exercicio_GEOD61_St3.mat')
print(annots)
con_list = [[element for element in upperElement] for upperElement in annots['time_adcp']]

#criando as variaveis
time_adcp=annots['time_adcp']
Vel=annots['Vel']
Vel=Vel[:,1:]
Dir=annots['Dir']
Dir=Dir[:,1:]

'''Criando os componentes da velocidade'''
# primeiro e necessario converter a direcao para radianos
Dir_rad=np.empty_like(Dir)
Dir_rad.fill(0)
for i in range(len(Dir_rad)):
    for j in range(0,29):
        Dir_rad[i,j]=math.radians(Dir[i,j])
        
# Criando componente U da velocidade
u=np.empty_like(Vel)
u.fill(0)
for i in range(len(Dir_rad)):
    for j in range(0,29):
        u[i,j]=Vel[i,j]*(math.sin(Dir_rad[i,j]))
# Criando componente V da velocidade
v=np.empty_like(Vel)
v.fill(0)
for i in range(len(Dir_rad)):
    for j in range(0,29):
        v[i,j]=Vel[i,j]*(math.cos(Dir_rad[i,j]))
        
'''Velocidade media na coluna d'agua'''
v_med=np.nanmean(v,axis=1)
'''plotando velocidade v e maré'''
fig,ax1=plt.subplots()
ax1.plot(time_adcp,v_med)
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Velocidade V (m/s)')
ax2=ax1.twinx()
ax2.plot(time_adcp,nivel_filt,color='orange')
ax2.set_ylabel('Nível (m)')
ax1.axhline(y = 0, color = 'r', linestyle = '-')
#adicionar legendas!
'''Calcular velocidades maximas de enchente e vazante'''
v_max_e = plt.ginput(23,timeout=0,show_clicks=True)
v_maxe = [tup[1] for tup in v_max_e]

v_max_v=plt.ginput(23,timeout=0,show_clicks=True)
v_maxv=[tup[1] for tup in v_max_v]
v_maxv=[i * (-1) for i in v_maxv]

'''Razão entre as velocidades maximas de enchente e vazante'''
razao_ev=[v_maxe/v_maxv for (v_maxv,v_maxe) in zip(v_maxv,v_maxe)]
plt.plot(razao_ev)
plt.title('Razão entre velocidades máximas de enchente e vazante')
plt.ylabel('Razão e/v')
plt.plot(v_maxe)
plt.plot(v_maxv)
