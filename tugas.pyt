# Mengimpor pustaka yang diperlukan
import numpy as np
import pandas as pd
from apyori import apriori


# Membaca dataset dari file Excel
data = pd.read_csv('GroceryStoreDataSet.csv')


# Menampilkan dataset
print(data)  


# Mengonversi dataset ke dalam format yang digunakan oleh algoritma Apriori
records = []
for i in range(data.shape[0]):
    records.append([str(data.values[i, j]).split(',') for j in range(data.shape[1])])

trx = [[] for trx in range(len(records))]
for i in range(len(records)):
    for j in records[i][0]:
        trx[i].append(j)


# Menampilkan dataset yang sudah diubah ke format yang sesuai
print(trx)  


# Menjalankan algoritma Apriori dengan parameter yang ditentukan
association_rules = apriori(trx, min_support=0.1, min_confidence=0.6, min_lift=1)
association_results = association_rules


# Menyiapkan DataFrame untuk menyimpan hasil aturan asosiasi
pd.set_option('max_colwidth', 1000)
Result = pd.DataFrame(columns=['Rule', 'Support', 'Confidence'])


# Memproses hasil aturan asosiasi dan menambahkannya ke DataFrame
for item in association_results:
    pair = item[2]
    for i in pair:
        items = str([x for x in i[0]])
        if i[3] != 1:
            Result = Result._append({
                'Rule': str([x for x in i[0]]) + " -> " + str([x for x in i[1]]),
                'Support': str(round(item[1]*100, 2))+'%',
                'Confidence': str(round(i[2] * 100, 2))+'%'
            }, ignore_index=True)


# Menampilkan hasil aturan asosiasi dalam bentuk DataFrame
print(Result)  
