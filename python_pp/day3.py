# Name, age, address create df
# If age less than 22 kk column

import pandas as df

records = [{'id':1, 'name':'hari', 'age':45},
           {'id':2, 'name':'krish', 'age':21},
           {'id':3, 'name':'ram', 'age':20},
           {'id':4, 'name':'jayam', 'age':25} ]

df_record = df.DataFrame(records, columns = ['id', 'name', 'age'])

records = df_record.to_dict("records")

new_records = []

for i in range(len(records)):
    if records[i]['age'] > 22:
        new_records.append(records[i])

print(df.DataFrame(new_records))

#output

#    id   name  age
# 0   1   hari   45
# 1   4  jayam   25