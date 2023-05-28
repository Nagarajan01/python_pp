# Column
# Name, 5 sub mark
# Avg venum aparm etho oru sub > 35 iruntha result fail varum ilana pass

import pandas as df


info = [{'id': 1, 'name': 'ramesh', 'subject' : {'tamil' : 45, 'english' : 58, 'maths' : 87, 'science' : 74, 'social' :47}},
        {'id': 2, 'name': 'suresh', 'subject' : {'tamil' : 87, 'english' : 25, 'maths' : 87, 'science' : 54, 'social' :32}},
        {'id': 3, 'name': 'sylesh', 'subject' : {'tamil' : 53, 'english' : 25, 'maths' : 87, 'science' : 89, 'social' :87}},
        {'id': 4, 'name': 'vignesh', 'subject' : {'tamil' : 47, 'english' : 74, 'maths' : 87, 'science' : 98, 'social' :97}}]

df_marks = df.DataFrame(info, index=[1, 2, 3, 4], columns=['id', 'name', 'subject'])

        #    id     name  english  tamil  maths  science  social
        # 1   1   ramesh       58     45     87       74      47
        # 2   2   suresh       25     87     87       54      32
        # 3   3   sylesh       58     53     87       89      87
        # 4   4  vignesh       74     47     87       98      97



df_records = df_marks.to_dict('records')

# [{'id': 1, 'name': 'ramesh', 'english': 58, 'tamil': 45, 'maths': 87, 'science': 74, 'social': 47}, 
#  {'id': 2, 'name': 'suresh', 'english': 25, 'tamil': 87, 'maths': 87, 'science': 54, 'social': 32},
#  {'id': 3, 'name': 'sylesh', 'english': 58, 'tamil': 53, 'maths': 87, 'science': 89, 'social': 87},
#  {'id': 4, 'name': 'vignesh', 'english': 74, 'tamil': 47, 'maths': 87, 'science': 98, 'social': 97}]


sub_keys = list(df_records[0]['subject'].keys())
dup_list = []
for i in range(len(df_records)):
    for j in sub_keys:
        if df_records[i]['name'] not in dup_list:
            if df_records[i]['subject'][j] <= 35:
                df_records[i]['average'] = 'fail'
            else:
                average = (sum([(df_records[i]['subject'][sub_keys]) for sub_keys in [sub for sub in sub_keys]]))
                df_records[i]['average'] = round((average / 500) * 100, 2)
print(df_records)
#output

# [{'id': 1, 'name': 'ramesh', 'subject': {'tamil': 45, 'english': 58, 'maths': 87, 'science': 74, 'social': 47}, 'average': 62.2},
#  {'id': 2, 'name': 'suresh', 'subject': {'tamil': 87, 'english': 25, 'maths': 87, 'science': 54, 'social': 32}, 'average': 'fail'},
#  {'id': 3, 'name': 'sylesh', 'subject': {'tamil': 53, 'english': 25, 'maths': 87, 'science': 89, 'social': 87}, 'average': 68.2},
#  {'id': 4, 'name': 'vignesh', 'subject': {'tamil': 47, 'english': 74, 'maths': 87, 'science': 98, 'social': 97}, 'average': 80.6}]