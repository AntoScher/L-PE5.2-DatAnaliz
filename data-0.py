import hashlib
import matplotlib.pyplot as plt  # Рекомендуется использовать общепринятое название переменной "plt"
#import numpy as np
import pandas as pd

doc_views = pd.read_csv('doc_views.csv')
payments = pd.read_excel('case_data.xlsx', sheet_name='Payments')
#print(doc_views.head())
#print(payments.head())
#print(payments.tail(10))
# Изменяем настройки отображения для полного вывода
"""pd.set_option('display.max_rows', None)       # Показывать все строки
pd.set_option('display.max_columns', None)    # Показывать все столбцы
pd.set_option('display.width', None)          # Не ограничивать ширину отображения
pd.set_option('display.max_colwidth', None)     # Не обрезать содержимое столбцов

print(doc_views.to_string())  # Выводим DataFrame полностью
print(payments.to_string())   # Выводим DataFrame полностью
"""
doc_views = doc_views.rename(columns={'Name':'name','Last Name':'last_name', 'Passport Number':'passport_number', 'ID':'id'})
#print(doc_views.to_string())
#print(doc_views.head())
#print(doc_views.info())

doc_views['viewed_at'] = pd.to_datetime(doc_views['viewed_at'])
#print(doc_views['viewed_at'])
doc_views['passport_number'] = doc_views['passport_number'].astype(str)
#print(doc_views.info())

payments.query('user_id.isna()')
payments.query("user_id.isna() == False")
payments = payments.query("user_id.isna() == False")
#print(payments.info())

payments['user_id'] = payments['user_id'].astype('int')
#print(payments.info())
doc_views.isna().sum()
#doc_views.query('category_name.isna()')
#print(doc_views.info())
#doc_views.query('category_name.isna() == False')[['category_id', 'category_name']]
#print(doc_views.head())
#doc_views.query('category_name.isna() == False')[['category_id', 'category_name']].drop_duplicates()

#print(doc_views.query('category_name.isna() == False')[['category_id', 'category_name']].drop_duplicates().reset_index(drop=True))
#print(doc_views.query('category_name.isna() == False')[['category_id', 'category_name']].drop_duplicates().reset_index(drop=True).set_index('category_id')['category_name'])
category_dict = doc_views.query('category_name.isna() == False')[['category_id', 'category_name']].drop_duplicates().reset_index(drop=True).set_index('category_id')['category_name']
#print(category_dict[10])
#pd.set_option('display.max_columns', None)    # Показывать все столбцы
def fill_nans(col_id): return category_dict[col_id]
doc_views['category_name'] = doc_views['category_id'].apply(fill_nans)
#print(doc_views.isna().sum())
#print(doc_views.query('category_name.isna() == True'))

def hash_passport(passport): return hashlib.sha256(passport.encode()).hexdigest()
doc_views['passport_number'] = doc_views['passport_number'].apply(hash_passport)

#pd.set_option('display.max_columns', None)    # Показывать все столбцы
#print(doc_views.head())
doc_views = doc_views.drop(columns='last_name')
#print(doc_views.head())

print(doc_views.duplicated().sum())
payments = payments.drop_duplicates()
print(payments.duplicated().sum())

doc_views.to_csv('doc_views_result.csv',index=False)
payments.to_csv('payments_result.csv',index=False)