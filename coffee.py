amount_due = 50
coins = [5,10,20,50]
while amount_due > 0:
     print(f'Нужная сумма: {amount_due}')
     coin = int(input('Вставьте монету: '))
     if coin in coins:
        amount_due -= coin;
print(f'Ваша сдача: {abs(amount_due)}')
