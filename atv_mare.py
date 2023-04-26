# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:13:52 2023

@author: jdebr
"""
'''Atividade da disciplina Dinâmica Estuarina - semestre 2023.1 '''
import numpy as np

#abrindo o arquivo em .mat
#https://www.askpython.com/python/examples/mat-files-in-python
from scipy.io import loadmat
annots = loadmat('C:/Users/jdebr/Documents/Oceanografia/Disciplinas/Dinâmica Estuarina/Exercicio_GEOD43.mat')
print(annots)
con_list = [[element for element in upperElement] for upperElement in annots['time_adcp']]

#criando as variaveis
time_adcp=annots['time_adcp']
nivel=annots['nivel']

#Filtrando os dados
'''how to smooth the data?'''
nivel_filt=np.empty_like(nivel)
nivel_filt.fill(0)
for i in range(len(nivel)):
    if nivel[i]<nivel[i-1] and nivel[i]<nivel[i+1]:
        nivel_filt[i]=(nivel[i+1]+nivel[i-1])/2
    else:
        nivel_filt[i]=nivel[i]

#Criando o grafico
import matplotlib.pyplot as plt
fig = plt.figure()
plt.suptitle('Variação de maré em metros',fontsize=16)
plt.plot(time_adcp,nivel_filt,'-',color='black')

#preamar

preamar=np.empty_like(nivel)
preamar.fill(0)

for i in range(1,1728):
    if i>0 and i<(len(preamar)):
        if (nivel_filt[i]>nivel_filt[i-1]) and (nivel_filt[i]>nivel_filt[i+1]):
            preamar[i]=nivel_filt[i]
        else:
            preamar[i]=np.nan
            
preamar[1060]=np.nan
preamar[909]=np.nan
preamar[686]=np.nan
preamar[611]=np.nan
preamar[538]=np.nan

for i in range(1,1728):
    if preamar[i]<7:
        preamar[i]=np.nan

plt.scatter(time_adcp,preamar,marker='.',color='red')


#baixamar
baixamar=np.empty_like(nivel)            
baixamar.fill(np.nan)
for i in range(1,1728):
    if i>0 and i<(len(baixamar)):
        if (nivel[i]<nivel[i-1]) and (nivel[i]<nivel[i+1]):
            baixamar[i]=nivel[i]

baixamar[24]=np.nan
baixamar[131]=np.nan
baixamar[205]=np.nan
#baixamar[318]=np.nan
baixamar[428]=np.nan
#baixamar[469]=np.nan
baixamar[504]=np.nan
#baixamar[540]=np.nan
baixamar[577]=np.nan
#baixamar[612]=np.nan
#baixamar[617]=np.nan
baixamar[646]=np.nan
baixamar[653]=np.nan
baixamar[719]=np.nan
baixamar[722]=np.nan
baixamar[726]=np.nan
baixamar[728]=np.nan
baixamar[871]=np.nan
baixamar[940]=np.nan
baixamar[947]=np.nan
baixamar[1020]=np.nan
baixamar[1091]=np.nan
baixamar[1097]=np.nan
baixamar[1099]=np.nan
baixamar[1173]=np.nan
baixamar[1178]=np.nan
baixamar[1244]=np.nan
baixamar[1251]=np.nan
baixamar[1254]=np.nan
baixamar[1257]=np.nan
baixamar[1322]=np.nan
baixamar[1326]=np.nan
baixamar[1398]=np.nan
baixamar[1401]=np.nan
baixamar[1406]=np.nan
baixamar[1329]=np.nan
baixamar[1480]=np.nan
baixamar[1628]=np.nan
baixamar[1706]=np.nan

for i in range(1,1728):
    if baixamar[i]>7:
        baixamar[i]=np.nan
plt.scatter(time_adcp,baixamar,color='blue')

#tempo de subida de maré
'''excluir nan e criar nova lista contendo os tempos e a altura da mare'''
#tempo de descida da maré 

