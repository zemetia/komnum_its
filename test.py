#from module.akolade.bolzano import Bolzano
from module.terbuka.newtonraphson import NewtonRaphson
import math
import pandas as pd

fungsi = lambda x: (0.667 * (x ** 3)) - (3.9 * (x ** 2)) + (6.21*x) - 2.1
d_fungsi = lambda x: (2.001 * (x ** 2)) - (7.8 * x) + 6.21
soal = NewtonRaphson(fungsi, d_fungsi)
df = pd.DataFrame(soal.data)
print(df)