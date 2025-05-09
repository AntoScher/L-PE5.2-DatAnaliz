import hashlib
import matplotlib.pyplot as plt  # Рекомендуется использовать общепринятое название переменной "plt"
import numpy as np
import pandas as pd

doc_views = pd.read_csv('doc_views.csv')
payments = pd.read_excel('case_data.xlsx', sheet_name='Payments')
print(doc_views.head())
print(payments.head())
print(payments.tail(10))
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
print(doc_views.head())
print(doc_views.info())

doc_views['viewed_at'] = pd.to_datetime(doc_views['viewed_at'])
print(doc_views['viewed_at'])
doc_views['passport_number'] = doc_views['passport_number'].astype(str)
print(doc_views.info())

print(payments.info())
#payments['user_id'] = payments['user_id'].astype('int')
payments.query('user_id.isna()')
print(payments.info())