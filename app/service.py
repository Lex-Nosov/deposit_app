import calendar


def deposit_calculation(date, periods, amount, rate) -> dict:
    deposit_total = {}
    d, m, y = map(int, date.split('.'))
    cur_sum = amount
    for i in range(periods):
        summ = cur_sum * (1 + (rate / 100) / 12)
        cur_sum = summ
        if m + i > 12:
            m -= 12
            y += 1
        day, month = (calendar.monthrange(year=y, month=m + i))[1], m + i
        deposit_total[f'{day}.{month}.{y}'] = round(cur_sum, 2)
    return deposit_total
