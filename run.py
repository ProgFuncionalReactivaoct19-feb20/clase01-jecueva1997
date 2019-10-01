"""
	autor: jecueva11
"""

from ejercicio import metodoUno
from ejercicio import metodoDos
from ejercicio import metodoTres
from ejercicio import metodoCuatro

print (metodoUno(3))

print(metodoDos(metodoUno(4)))

print(metodoTres(metodoDos(metodoTres(5))))

print(metodoCuatro(metodoTres(metodoDos(metodoUno(2)))))



