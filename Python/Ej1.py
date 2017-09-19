# -*- coding: utf-8 -*-
"""
Ej1 Python

 hacer un programa que reciba por linea de comandos un archivo a procesar, y 
 analice los datos de cada sensor por separado. Para cada sensor se debera 
 calcular el promedio y la desviacion estandar, y luego indicar que
 valores tienen una diferencia con el promedio mas grande que tres sigma 
 (y a que hora se sucedieron).

@author: humberto.celleri
"""

import numpy as np
import sys
import argparse

class oven_temperature:    
    """
    (Unpure) class of oven read temperatures 
    """
    def __init__(self, file_name):
        """
        Method to initialize class
        """
        self.file_name = file_name
        
        try: # Catch if name is wrong
            with open(file_name, 'rb') as f:
                self.data= self.read_file(f)
            
        except IOError:
            print "Could not read file:", file_name

        self.prom = []
        self.stddev= []
        self.out_of_3stddev = []
        
    def read_file(self,file_name):
        """
        Function that returns a data structure generated with np.genfromtxt
        """
        data = np.genfromtxt(file_name)
        return data;
    
    def compute_analysis(self):
        """
        Method to compute all the necesary analysis
        """
        def get_mean(self):
            """
            Compute mean in all sensors
            """
            for i in range(1,len(self.data[0])):
                self.prom.append(np.mean(self.data[:,i])) 

        
        def get_stddev(self):
            """
            Compute mean in all sensors
            """
            for i in range(1,len(self.data[0])):
                self.stddev.append(np.std(self.data[:,i])) 
        
        # Get the values
        get_mean(self)
        get_stddev(self)
        
        # Check condition
        [(self.out_of_3stddev.append(i)) 
            for (i) in (self.data[:,0:4]) 
                if (any(
                (i[1:4] > 3*np.array(self.stddev)+np.array(self.prom))|
                (i[1:4] < -3*np.array(self.stddev)+np.array(self.prom))
                ))]
       
        
    def display_results(self):
        """
        Display results
        """
        print("Los valores que se encontraron fuera de 3 desviaciones estandar son:")
        for i in self.out_of_3stddev:
            print(i)
            

if __name__ == "__main__":
    """
    Analizar sensores por separado ( promedio y desv std, analizar si tienen 
    diferencia mayor a 3 sigma y hora del evento)
    """
    # INPUT VARIABLES: String con el nombre del archivo
    # Inicializa el lector de sys.arg: contiene todas las variables pasadas por 
    # linea de comandos
    parser = argparse.ArgumentParser(description='Process some integers.')   
    # Agregamos un argumento requerido (Si no está, da error)
    parser.add_argument('file_name', metavar='FileName', type=str, nargs='+',
                    help='str: A file name of the .txt containing tme and temperatures')
    # Guardamos las variables pasadas por comando
    args = parser.parse_args()

    # COMPUTE
    temperature_today = oven_temperature(args.file_name[0]) 
    
    temperature_today.compute_analysis()
    
    temperature_today.display_results()
    
    print("DONE!")