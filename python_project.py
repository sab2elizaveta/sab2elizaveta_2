# Для датафрейма log из материалов занятия создайте столбец source_type по правилам:

# если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
# для источников paid и email из России ставим ad;
# для источников paid и email не из России ставим other;
# все остальные варианты берём из traffic_source без изменений.


import pandas as pd 


data_log = pd.read_csv('C:\\Users\\hia14\\OneDrive\\Рабочий стол\\Python\\visit_log.csv',encoding='utf-8', delimiter=';')

data_log['source_type'] = data_log['traffic_source']

data_log.loc[(data_log['traffic_source'] == 'yandex') | (data_log['traffic_source'] == 'google'), 'source_type'] = 'organic'

data_log.loc[((data_log['traffic_source'] == 'paid') | (data_log['traffic_source'] == 'email')) & (data_log['region'] == 'Russia'), 'source_type'] = 'ad'

data_log.loc[((data_log['traffic_source'] == 'paid') | (data_log['traffic_source'] == 'email')) & (data_log['region'] != 'Russia'), 'source_type'] = 'other'


# В файле URLs.txt содержатся URL страниц новостного сайта. Вам нужно отфильтровать его по адресам страниц с текстами новостей. 
# Известно, что шаблон страницы новостей имеет внутри URL конструкцию: /, затем 8 цифр, затем дефис.


data_url = pd.read_csv('C:\\Users\\hia14\\OneDrive\\Рабочий стол\\Python\\URLs.txt', encoding='utf-8')

regulal = r'/\d{8}-'

filtered_url = data_url.loc[data_url['url'].str.contains(regulal)]

print(filtered_url.head(15))

# Используйте файл с оценками фильмов ml-latest-small/ratings.csv. 
# Посчитайте среднее время жизни пользователей, которые выставили более 100 оценок. 
# Под временем жизни понимается разница между максимальным и минимальным значениями столбца timestamp для данного значения userId.

import numpy as np

data_ratings = pd.read_csv('C:\\Users\\hia14\\OneDrive\\Рабочий стол\\Python\\ml-latest-small\\ratings.csv', encoding='utf-8')

min_max = data_ratings.groupby('userId')['timestamp'].agg(['count', np.ptp])

time_life = min_max.loc[min_max['count'] > 100].mean()

print(time_life)

# Нужно сформировать две таблицы:
# - таблицу с тремя типами выручки для каждого client_id без указания адреса клиента;
# - аналогичную таблицу по типам выручки с указанием адреса клиента.

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
rzd

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
auto

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
air

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

new_table = client_base[['client_id']].copy()

new_table = new_table.merge(rzd, how = 'left', left_on='client_id', right_on='client_id')

new_table = new_table.merge(auto, how = 'left', left_on='client_id', right_on='client_id')

new_table = new_table.merge(air, how = 'left', left_on='client_id', right_on='client_id')

print(new_table)

table_address = new_table.merge(client_base, how = 'left', left_on='client_id', right_on='client_id')

print(table_address)
