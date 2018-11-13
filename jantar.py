from filosofo import Filosofo
# from filosofo2 import Filosofo
from garfo import Garfo
import threading

g = list()
for i in range(5):
    g.append(Garfo(i))

f1 = Filosofo(1, 'Aristóteles', g[0], g[1])
f2 = Filosofo(2, 'Platão', g[1], g[2])
f3 = Filosofo(3, 'René Descartes', g[2], g[3])
f4 = Filosofo(4, 'Jean-Jacques Rousseau', g[3], g[4])
f5 = Filosofo(5, 'Thomas Hobbes', g[4], g[0])

f1.start()
f2.start()
f3.start()
f4.start()
f5.start()
