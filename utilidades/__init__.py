#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from datetime import date, timedelta
import importlib
import sqlite3
import os
import requests
import xlrd
import sys
import matplotlib.pyplot as plt


UTILIDADES_OK           =0
UTILIDAD_TAM_BUFFER     =4096

    
#########################################################################################
#
#                                 Código de la librería
#
#########################################################################################

def imprimir_stderr(*cosas):
    print(*cosas, file=sys.stderr)

def existe_fichero(nombre_fichero):
    if (os.path.isfile(nombre_fichero)):
        return True
    return False

"""Descarga un archivo desde una url y lo guarda en el nombre de archivo indicado"""
def descargar_archivo(url, nombre_archivo_destino):
    peticion=requests.get(url)
    with open(nombre_archivo_destino, 'wb') as fd:
        for chunk in peticion.iter_content(UTILIDAD_TAM_BUFFER):
            fd.write(chunk)
    return UTILIDADES_OK

"""Descarga un archivo desde una URL solo en el caso de que el archivo no existiera"""
def descargar_archivo_si_no_existe(url, nombre_archivo_destino):
    if (existe_fichero(nombre_archivo_destino)):
        return
    return descargar_archivo(url, nombre_archivo_destino)

"""Genera una lista de fechas empezando en cierto día del año y hasta el dia de hoy"""
def generar_lista_fechas(dia, mes, anio):
    #Formato:
    # %Y año con cuatro cifras
    # %m mes con dos cifras
    # %d dia con dos cifras
    # %a Dia de la semana en idioma local "Sun", "Mon"
    # %A Dia de la semana en idioma local "Sunday", "Monday"
    
    formato="%Y%m%d"
    lista_fechas=[]
    fecha=date(anio, mes, dia)
    hoy=date.today()
    incremento=timedelta(days=1)
    while (fecha<=hoy):
        lista_fechas.append(fecha.strftime(formato))
        fecha=fecha+incremento
    return lista_fechas

class LibroExcel(object):
    """Abrir un archivo Excel que se asume que está en formato Unicode (Excel 97 y posteriores)"""
    def __init__(self, nombre_archivo_excel):
        self.nombre_archivo=nombre_archivo_excel
        archivo_logs="Errores_en_archivo_XLS "+nombre_archivo_excel
        self.archivo_fd=open(archivo_logs, "w")
        self.libro=xlrd.open_workbook(nombre_archivo_excel, logfile=self.archivo_fd)
    """Indica de que hoja vamos a leer celdas, la primera es la 0"""
    def marcar_hoja_como_activa(self, num_hoja):
        self.hoja=self.libro.sheet_by_index(num_hoja)
        
    def leer_celda(self, fila, columna):
        if (self.hoja==None):
            raise IOError("No hay hojas activas (¿olvidó llamar a marcar_hoja_como_activa)")
        
        valor_celda=self.hoja.cell_value(fila, columna)
        return valor_celda
    


class BD(object):
    def __init__(self, archivo_bd):
        self.conexion=sqlite3.connect(archivo_bd)
        self.cursor=self.conexion.cursor()
        
    def ejecutar_sql(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def convertir_a_fila(self, lista_tuplas):
        lista=[]
        for tupla in lista_tuplas:
            lista.append(tupla[0])
        return lista
    
    def extraer_fila_valores(self, sql):
        fila_tuplas=self.ejecutar_sql(sql)
        fila_valores=self.convertir_a_fila(fila_tuplas)
        return fila_valores
    
    def extraer_valor_unico(self, sql):
        filas=self.ejecutar_sql(sql)
        #print (filas)
        return filas[0][0]
        
def crear_grafico_lineas(lista_x, lista_y, nombre_archivo="archivo.png", leyenda_x="", leyenda_y="", titulo=""):
    plt.clf()
    grafico, =plt.plot(lista_x, lista_y)
    
    plt.xlabel(leyenda_x)
    plt.ylabel(leyenda_y)
    plt.title(titulo)
    plt.savefig(nombre_archivo)
    
    
def rellenar_plantilla(fichero_plantilla, diccionario_valores):
    pass
