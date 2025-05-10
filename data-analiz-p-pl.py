import matplotlib.pyplot as plt  # Рекомендуется использовать общепринятое название переменной "plt"
import pandas as pd

payments = pd.read_csv('payments_result.csv')

#pint(payments['shopper_locale'].unique())
#print(payments.currency.unique())
#pd.set_option('display.max_rows', None)       # Показывать все строки
#pd.set_option('display.max_columns', None)    # Показывать все столбцы
#print(payments.groupby('shopper_locale')['amount'].sum())

locale_amounts = payments.groupby('shopper_locale')['amount'].sum()
plt.figure(figsize=(10, 6)) # Задаем размер графика
locale_amounts.plot(kind='bar', color='skyblue') # Создаем столбчатую диаграмму
plt.title('Сумма платежей по локациям покупателей') # Заголовок диаграммы
plt.xlabel('Локация покупателя') # Подпись оси Х
plt.ylabel('Сумма платежей') # Подпись оси Y
plt.xticks(rotation=45) # Поворот подписей на оси X для лучшей читаемости
plt.grid(True) # Включаем сетку для удобства восприятия
plt.show()