"""
Получите первый и последний элемент списка
"""

"""Версия 2"""
def power():
    a = input("Введите значения списка: ")
    result = a.split()
    print(result)

    print(result[0])
    print(result[-1])


if __name__ == '__main__':
    power()
