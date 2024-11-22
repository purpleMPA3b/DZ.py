import re

def command(command, array):

    match = re.fullmatch(r"Получить элемент по (\d+) индексу", command)
    if match:
        index = int(match.group(1))
        if 0 <= index < len(array):
            return array[index]
        return "Ошибка: индекс выходит за границы массива."

    match = re.fullmatch(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        step = int(match.group(3))
        if start < 0 or end > len(array) or step <= 0:
            return "Ошибка: некорректные границы или шаг."
        return array[start:end:step]

    match = re.fullmatch(r"Получить (\d+)-ый элемент с конца массива", command)
    if match:
        n = int(match.group(1))
        if 1 <= n <= len(array):
            return array[-n]
        return "Ошибка: некорректный номер элемента."

    return "Ошибка: команда не распознана."

# Тестирование
if __name__ == "__main__":
    someArray = [10, 20, 30, 40, 50, 60 ]

    print(command("Получить элемент по 2 индексу", someArray))  #30
    print(command("Получить элементы с 1 по 5 с шагом 2", someArray))  #20, 40
    print(command("Получить 3-ый элемент с конца массива", someArray))  #50
    print(command("Получить элемент по 10 индексу", someArray))  #Ошибка
    print(command("Получить элементы с 1 по 10 с шагом 2", someArray))  #Ошибка
    print(command("  ", someArray))