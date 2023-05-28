# Sari rendu df

# A and b

# A la id, name, age
# B la salary, name, id


# B layum A layum same iruka namesoda age B la varanum

import pandas as pd

data_1 = [[1, "naga", 23], [2, "venkat", 23], [3, "bala", 23], [4, "hari", 23]]
data_2 = [[1, "naga", "20k"], [2, "venkat", "23k"], [3, "bala", "23k"], [4, "kanna", "23k"]]


df_age = pd.DataFrame(data_1, columns=['id', 'name', 'age'])
df_salary = pd.DataFrame(data_2, columns=['id', 'name', 'salary'])

# print(df_age.merge(df_salary, left_on = 'id', right_on = 'id'))


df_age = df_age.to_dict()
df_salary = df_salary.to_dict('records')

print(df_salary, "df to dict")


df_new_salary = {}
df_new_salary['age'] = {}

for i in df_age['name']:
    if str(df_age['name'][i]) in [df_salary['name'][j] for j in range(len(df_salary))]:
        df_new_salary[i] = df_age['age'][i]
        
df_salary['age']=df_new_salary

#output of df_salary
    # {'id': {0: 1, 1: 2, 2: 3, 3: 4}, 'name': {0: 'naga', 1: 'venkat', 2: 'bala', 3: 'kanna'}, 
    #  'salary': {0: '20k', 1: '23k', 2: '23k', 3: '23k'}, 'age': {'age': {0: 23, 1: 23, 2: 23}}}

df_salary = pd.DataFrame(df_salary, columns=['id', 'name', 'salary', 'age'], index = [0, 1, 2, 3])

# print(df_salary)

#output
            #     id    name salary   age
            # 0  1.0    naga    20k  23.0
            # 1  2.0  venkat    23k  23.0
            # 2  3.0    bala    23k  23.0
            # 3  4.0   kanna    23k   NaN
            # 4  NaN     NaN    NaN   NaN



