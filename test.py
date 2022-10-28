#from module.akolade.bolzano import Bolzano
from module.akolade.regula_falsi import RegulaFalsi
from module.terbuka.fixed_point_iteration import FixedPointIteration
from module.terbuka.secant import Secant
import math
import pandas as pd
fungsi = lambda x: math.e**(-x) - x
soal = Secant(fungsi)
df = pd.DataFrame(soal.data)
print(df)