try:
    a = 100
    b = int(input("Введите число: "))
    c = a / b
except ZeroDivisionError:
    c = 0
    print("Ошибка! c= " , str(c))
print("100 / ", b, "= ", round(c))
