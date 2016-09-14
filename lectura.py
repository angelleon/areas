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

from areas import *
import os

try:
	os.system("rm der1.txt der2.txt izq1.txt izq2.txt")
except Eception:
	pass
f_der1 = open("der1.txt", "w")
f_der2 = open("der2.txt", "w")
f_izq1 = open("izq1.txt", "w")
f_izq2 = open("izq2.txt", "w")

for i in range(1, 101):
	der1 = area(4, [0.1, -2.38, 18.7, -55.4, 109.37], 0, 10, i, "d")
	der2 = area(4, [0.05, -0.9, 4.15, -0.8, 35.05], 0, 10, i, "d")
	izq1 = area(4, [0.1, -2.38, 18.7, -55.4, 109.37], 0, 10, i, "i")
	izq2 = area(4, [0.05, -0.9, 4.15, -0.8, 35.05], 0, 10, i, "i")
	f_der1.write(str(i) + "\t" + str(der1) + "\n")
	f_der2.write(str(i) + "\t" + str(der2) + "\n")
	f_izq1.write(str(i) + "\t" + str(izq1) + "\n")
	f_izq2.write(str(i) + "\t" + str(izq2) + "\n")

	print("El área por derecha de la primera función es:")
	print (der1, " aproximadamente\n")
	print("El área por izquierda de la primera función es:")
	print (izq1, " aproximadamente\n")
	print("El área por derecha de la segunda función es:")
	print (der2, " aproximadamente\n")
	print("El área por derecha de la segunda función es:")
	print (izq2, " aproximadamente\n")
	print("-------------------------------------------------------\n")

f_der1.close()
f_der2.close()
f_izq1.close()
f_izq2.close()
