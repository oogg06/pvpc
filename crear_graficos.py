#!/usr/bin/python3
# -*- coding: utf-8 -*-


import utilidades
from utilidades import *

bd=BD("valores.db")
valor=bd.extraer_valor_unico("select max(precio) from valores")



y=bd.extraer_fila_valores(
    "select avg(precio) from valores group by fecha order by fecha")
x=range(0, len(y))

crear_grafico_lineas(x, y, "PrecioDiario.png", "Tiempo (en dias)", "Precio (en euros)", "Evolucion del precio diario")

meses=range(4, 13)
valores_medios_por_mes=bd.extraer_fila_valores(
    "select avg(precio) from valores group by strftime('%m', fecha) order by strftime('%m', fecha)")

crear_grafico_lineas(meses, valores_medios_por_mes, "PrecioMedioMensual.png", "Mes (4=abr, 12=dic)", "Precio (en euros)", "Evolucion del precio mensual")

y=bd.extraer_fila_valores(
    "select avg(precio) from valores group by hora order by hora")
x=range(0, len(y))
crear_grafico_lineas(x, y, "PrecioDuranteDia.png", "Tiempo (en horas)", "Precio (en euros)", "Precio medio por hora del dia")



y=bd.extraer_fila_valores(
    "select avg(precio) from valores group by strftime('%w', fecha) order by strftime('%w', fecha)")
x=range(0, len(y))
crear_grafico_lineas(x, y, "PrecioDiaSemana.png", "Dia(0=Lun, 6=Dom)", "Precio medio (en euros)", "Precio medio por dia semana")


