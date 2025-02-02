# -*- coding: utf-8 -*-
"""Study Case 01 ( EDA )

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g6xcuM9E9Y7ehyvraTrH1dAADb5QCm6W

###**KELOMPOK 7**
1.   Rizqi Maulidi (112109400000
2.   Lariesa Ananda Putri (11210940000006)
3. Della Wiyanti (11210940000014)
4. Heny Rosyidatun (11210940000016)
5. Nadya Rifqah

###**1. IMPORT DATA**
Meletakkan file data 'datadepok.csv' dengan diketik %pwd di syntax.
"""

import pandas as pd, matplotlib.pyplot as plt, seaborn as sns, numpy as np

"""Keterangan Varabel:

Created_at: Tanggal dimana iklan rumah dibuat
LT : Luas Tanah properti yang ditawarkan\
LB : Luas Bangunan properti yang ditawarkan
KT : Jumlah Kamar Tidur properti yang ditawarkan\
KM : Jumlah Kamar Mandi properti yang ditawarkan\
Garasi : Jumlah Kapasitas Garasi di properti yang ditawarkan\
Carport : Kapasitas Carport di properti yang ditawarkan\
Lokasi : Detail lokasi properti yang ditawarkan\
Sertifikat: sertifikat Jenis properti yang ditawarkan\
Listrik : Daya listrik dari properti yang ditawarkan\
Hadap : Keterangan properti yang ditawarkan menghadap ke arah mana\
Harga : Harga property yang ditawarkan dalam Rupiah\
URL : Alamat tautan (link) properti yang ditawarkan.\
Deskripsi : Deskripsi properti iklan yang ditawarkan.\

"""

datadepok = pd.read_csv('depok.csv')
datadepok

datadepok.info()

datadepok.describe().T

"""###**2. DATA PREPROCESSING**

#####**Mengubah Variabel created_at menjadi index**
"""

datadepok = pd.read_csv('depok.csv', parse_dates = True, index_col = "created_at", low_memory = False)
datadepok

datadepok.info()

"""#####**Missing Value**"""

datadepok.isnull().sum()

"""Terdapat 3 missing value pada data yang diinput, yaitu untuk variabel **garasi**, **carport**, dan **hadap**.
Untuk variabel **garasi** dan **carport** yang mana seharusnya tercantum angka apapun dan pada data ini, variabel **garasi** dan **carport** terdefinisi sebagai NaN. Maka kedua variabel tersebut haruslah diganti dengan angka **nol** atau **0**.

Selanjutnya untuk variabel **hadap**, variabel tersebut juga terdapat data yang tidak tercantum angka apapun. Namun kami tidak akan mengubah missing value pada variabel **hadap** menjadi angka **nol** atau **0**. Hal ini dikarenakan terdapat kemungkinan untuk penjual rumah yang sengaja tidak menginput data atau lupa menginput data. Dan tidak mungkin pula sebuah rumah tidak memiliki arah atau hadap bangunannya, sehingga kami tidak akan mengubah apapun pada variabel **hadap**.
"""

datadepok["garasi"].fillna(0, inplace = True)
datadepok["sertifikat"].fillna(0, inplace = True)
datadepok["hadap"].fillna(0, inplace = True)

datadepok.isnull().sum()

"""Menghapus kolom yang tidak terpakai"""

datadepok1 = datadepok.loc[:, ~datadepok.columns.str.contains('^Unnamed')]
datadepok1