# Accolade Method
Contributor:
- Yoel Mountanus Sitorus ( zemetia )

# How to Use
pastikan/download module yang diperlukan yaitu `numpy`
Pertama-tama import modulenya
```py
from integrasi.trapezoida import Trapezoida
from integrasi.simpson import Simpson
from integrasi.kuadratur import Kuadratur
```

Persiapkan fungsi yang akan di proses<br />
dengan contoh seperti dibawah
```py
fungsi = lambda x: math.pow(math.e, x)

#            ATAU

def fungsi(x): return math.pow(math.e, x)
```

setiap module menggunakan cara yang berbeda untuk pengoprasian

## Trapezoida
```py
from integrasi.trapezoida import Trapezoida

#Trapezoida(function, bottomBound: float, topBound: float)
fungsi = lambda x: math.pow(math.e, x)
trapezoida = Trapezoida(fungsi, 1, 3)
result = trapezoida.generate(section=2) #default section adalah 5
print(result['integration'], result['tipCorrection'])

```
akan mendapatkan result dari hasil integrasi fungsi yang diberikan

## Simpson

Simpson memiliki 2 fungsi untuk menghitung integrasi<br />
yaitu 1/3 `.computeOnePerThree(section)` dan 3/8 `.computeThreePerEight(section)`
```py
from integrasi.simpson import Simpson

#Simpson(function, bottomBound: float, topBound: float)
fungsi = lambda x: math.pow(math.e, x)
simpson = Simpson(fungsi, 1, 3)

# keakuratan hasil dari penggunaan 1/3 dan 3/8 tergantung dari fungsi yang di berikan
resultOPT = simpson.computeOnePerThree() #default section adalah 5
resultTPE = simpson.computeThreePerEight(10) #default section adalah 5
print(resultOPT, resultTPE)
```

## Kuadratur

Metode kuadratur merupakan metode yang paling sederhana dalam komputasi</br>
tidak memiliki section seperti 2 metode sebelumnya
```
from integrasi.kuadratur import Kuadratur

fungsi = lambda x: math.pow(math.e, x)
kuadratur = Kuadratur(fungsi, 1, 3)
print(kuadratur.computeIntegration())
```
