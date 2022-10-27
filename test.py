#from module.bolzano import Bolzano
from module.regula_falsi import RegulaFalsi
import pandas as pd
fungsi = lambda x: (1 - (0.6)*x) / x
soal1 = RegulaFalsi(fungsi, 1, 2)
df = pd.DataFrame(soal1.data)
print(df)