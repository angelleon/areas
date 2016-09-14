#!/bin/env python3
# -*- coding: utf8 -*-
#  areas.py
#  
#  Copyright 2016 Ángel León
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


def poly(grado, coef, x):
	imagen = 0;
	exp = grado;
	for i in coef:
		imagen += i * (x ** exp)
		exp -= 1
	return imagen


def suma_imagenes(grado, coef, a, b, n, deltaX, extremo):
	suma = 0;
	for i in range(1, n + 1):
		if extremo == 'd':
			suma += poly(grado, coef, a + (i * deltaX))
		else:
			suma += poly(grado, coef, a + ((i-1) * deltaX))
	return suma



def area(grado, coef, a, b, n, extremo="d"):
	deltaX = 0
	try:
		n = int(n)
		if type(a) == 'str' or type(b) == 'str':
			raise Exception
	except Exception:
		print("Debe introducir valores numéricos")
		return None

	if n == 0:
		print("El número de prticiones no puede ser cero, se ha tomado n = 1")
		n = 1
	elif n < 0:
		print("El número de particiones no puede ser negativo, se ha tomdo n = %i" % (0 - n))

	if a == b:
		return 0;
	elif a > b:
		c = a
		a = b
		b = c
		del c

	deltaX = (b - a) / n
	return suma_imagenes(grado, coef, a, b, n, deltaX, extremo) * deltaX

if __name__ == "__main__":
	while True:
		print("Introduzca el grado de su polinomio")
		grado = input()
		if type(grado) != 'int':
			print("El grado debe ser un número entero positivo")
			continue
		coef = []
		
#		for i in range(0, grado):
			
