"""
andresvallejoz1991
"""
from ejemplopython1 import metodoUno
from ejemplopython1 import metodoDos
from ejemplopython1 import metodoTres
from ejemplopython1 import metodoCuatro


print (metodoUno(3))

print (metodoDos(metodoUno(4)))

print (metodoTres(metodoDos(metodoTres(5))))

print (metodoCuatro(metodoTres(metodoDos(metodoUno(2)))))

