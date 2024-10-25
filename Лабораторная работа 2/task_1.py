money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0
expenses = spend
while money_capital + salary > expenses:
    if count == 0:
        money_capital += salary - expenses
        count += 1
    else:
        expenses += expenses * increase
        money_capital += salary - expenses
        count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
