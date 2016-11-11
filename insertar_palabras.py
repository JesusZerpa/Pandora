#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ZerpaCorp.zdb2 as zdb2
 
entrada=""
data=zdb2.zdb()
data.cargar("Palabras")
data.crear_tabla("Diccionario")
data.crear_campos("Diccionario",data.campo("Palabra",str),data.campo("Significado",str))

while entrada!="salir()":
    entrada=raw_input("Nueva Palabra: ")
    if entrada != "" and entrada != " " and entrada != "salir()":
        data.insertar_campos("Diccionario",entrada,"None",True)

    
        
    
