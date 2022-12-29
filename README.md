# Task-17.7.3
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму\n'))
percent = list(per_cent.values())
deposit = list(map(lambda num: num * money * 0.01, percent)) #Скорее всего решение корявое, но я обещаю научиться))
print('Сумма прибыли по вкладам в банках', deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))
