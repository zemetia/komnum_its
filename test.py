from module.bolzano import Bolzano
import pandas as pd
fungsi = lambda x: x*x*x - 3*x - 1
soal1 = Bolzano(fungsi, 1, 5)
soal1.generate(10)
df = pd.DataFrame(soal1.data)
print(df)