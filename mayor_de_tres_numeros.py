#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
num1 = 0
num2 = 0 
num3 = 0

#lectura de datos
num1 = int( input("Ingrese num1 \n") )
num2 = int( input("Ingrese num2 \n") )
num3 = int( input("Ingrese num3 \n") )

#operaciones
if( num1 > num2 and num1 > num3 ):
    print("El mayor es: ",num1)
    
if( num2 > num1 and num2 > num3 ):
    print("El mayor es: ",num2)
    
if( num3 > num1 and num3 > num2 ):
    print("El mayor es: ",num3)
    
  
    
  
    
  
    