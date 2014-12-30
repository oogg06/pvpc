#!/usr/bin/python3
# -*- coding: utf-8 -*-


import utilidades
from utilidades import *



def descargar_archivos():
    url_base="http://www.esios.ree.es/Solicitar?fileName=PVPC_DETALLE_DD_{0}&fileType=xls&idioma=es"
    #Se empezaron a colgar las hojas 1 de abril de 2014
    fechas=generar_lista_fechas(1,4,2014)
    
    #Se tienen todas las posibles fechas desde ese día hasta hoy
    #en una lista llamada fechas en formato YYYYMMDD
    
    #Se descargan todos los archivos
    for fecha in fechas:
        url=url_base.format(fecha)
        nombre_archivo=fecha+".xls"
        #imprimir_stderr("Descargando " + url)
        descargar_archivo_si_no_existe(url, nombre_archivo)
        

       
descargar_archivos()

