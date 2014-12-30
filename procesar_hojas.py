#!/usr/bin/python3
# -*- coding: utf-8 -*-


import utilidades
from utilidades import *


def procesar_hoja_calculo(archivo_xls):
    anio=archivo_xls[0:4]
    mes=archivo_xls[4:6]
    dia=archivo_xls[6:8]
    libro=LibroExcel(archivo_xls)
    libro.marcar_hoja_como_activa(0)
    fila_inicial=5
    fila_final=29
    col_fecha=0
    col_hora=1
    col_precio=4
    sentencia="insert into valores values ({0}, {1}, {2});"
    hora=1
    for fila in range(fila_inicial, fila_final):
        fecha="'{0}-{1}-{2}'".format(anio, mes, dia)
        precio=libro.leer_celda(fila, col_precio)
        print (sentencia.format(fecha, hora, precio))
        hora=hora+1

def procesar_archivos():
    print ("Begin transaction;")
    fechas=generar_lista_fechas(1, 4, 2014)
    for fecha in fechas:
        procesar_hoja_calculo(fecha+".xls")
    print ("End transaction;")



procesar_archivos()

#procesar_hoja_calculo("20141219.xls")

