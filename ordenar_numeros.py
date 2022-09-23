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
print("\n")
#operaciones 

#el menor 
if( num1 < num2 and num1 < num3 ):
    print(num1) 
if( num2 < num1 and num2 < num3 ):
    print(num2) 
if( num3 < num1 and num3 < num2 ):
    print(num3)
    
#el medio 

#2,1,3
if(num1 > num2 and num2 < num3 and num1 < num3):
    print(num1)
#num1 ,num2, num3
# 2   , 3   ,  1
if(num1 < num2 and num2 > num3 and num1 > num3):
    print(num1)
#1,2,3
if(num1<num2 and num2<num3 and num1<num3):
    print(num2)
#3,2,1
if(num1>num2 and num2>num3 and num1>num3):
    print(num2)
#1,3,2
if(num1<num2 and num2>num3 and num1 < num3):
    print(num3)
#3,1,2   
if(num1>num2 and num2<num3 and num1 > num3):
    print(num3)
    
#el mayor
if( num1 > num2 and num1 > num3 ):
    print(num1) 
if( num2 > num1 and num2 > num3 ):
    print(num2) 
if( num3 > num1 and num3 > num2 ):
    print(num3)



    
    