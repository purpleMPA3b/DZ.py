def PoiskMax (b, c):
    a = float (input ("Введите число a: " ))

    if a > 0:
        return max (a, b, c)
    else:
        return -1

result = PoiskMax (10, 13)
print ("Результат:", result)