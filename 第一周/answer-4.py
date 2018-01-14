price = 24.95  # 美元
discount = 0.4


def total(n):
    cost_book = (1.0 - discount) * n
    cost_ship = 3 + (n - 1) * 0.75
    return cost_book + cost_ship


book_amount = 60
sum = total(book_amount)
print("%d本书总计金额：" % book_amount, sum)
