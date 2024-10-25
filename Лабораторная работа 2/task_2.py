salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
expenses = spend
for num_month in range(1, months + 1):
    if num_month == 1:
        money_capital += expenses - salary
    else:
        expenses += expenses * increase
        money_capital += expenses - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
