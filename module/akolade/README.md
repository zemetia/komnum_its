# Accolade Method
Contribution:
- Yoel Mountanus Sitorus ( zemetia )

# How to Use
Pertama-tama import modulenya
```py
from akolade.tabulasi import Tabulasi
from akolade.bolzano import Bolzano
from akolade.regula_falsi import RegulaFalsi
```
<br />

Persiapkan fungsi yang akan di proses<br />
dengan contoh seperti dibawah
```py
fungsi = lambda x: (1 - (0.6)*x) / x

#            ATAU

def fungsi(x): return (1 - (0.6)*x) / x
```
<br />

Sebagai contoh akan menggunakan salah satu module<br />
dan menampilkannya menggunakan pandas
```py
from akolade.regula_falsi import RegulaFalsi
import pandas as pd

#RegulaFalsi(function, bottomBound: float, topBound: float)
fungsi = lambda x: (1 - (0.6)*x) / x
regula = RegulaFalsi(fungsi, 1, 2)

#class dari metode akan otomatis generate hasil sebanyak 5 iterasi pada initialisasi
table = pd.DataFrame(regula.data)
print(table)
```
<br />
Pada saat initialisasi `RegulaFalsi(...)` secara otomatis akan generate 5 iterasi <br />
kita dapat menggunakan fungsi `generate(iteration: int)` untuk generate data lagi

```py
regula.generate(10)
table = pd.DataFrame(regula.data)
print(table)
```
<br />
contoh hasil dari code diatas <br />
<img src="https://github.com/zemetia/komnum_its/blob/metode_akolade/src/images/accolade_regulafalsi_result.png">
