# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:51:57 2020

@author: Edison Andres
"""

# Funcion de Membresia Triangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se define un array x para el manejo del factor de calidad de un restaurante
x = np.arange(0, 11, 1)

# Se define un array para la funcion miembro de tipo triangular
calidad = sk.trimf(x, [0, 0, 0])

# Se grafica la funcion de membresia 
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del Servivio en un Restaurante')
plt.ylabel('Membresia')
plt.xlabel('Nivel de Servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)  