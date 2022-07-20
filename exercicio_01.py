import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


mes = ['Jan/2017', 'Fev/2017', 'Mar/2017', 'Abril/2017', 'Mai/2017', 'Jun/2017', 'Jul/2017',
        'Ago/2017', 'Set/2017', 'Out/2017', 'Nov/2017', 'Dez/2017']
ingressos = [363722, 146970, 163998, 261680, 189010, 146175, 394642, 159279, 116850, 226891, 118420, 169957]

plt.plot(mes, ingressos)

plt.show()
plt.clf()

plt.plot(ingressos, mes)
plt.show()

