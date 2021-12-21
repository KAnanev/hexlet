"""

Реализуйте функцию stringify(), похожую на JSON.stringify(), но со следующими отличиями:
ключи и строковые значения должны быть без кавычек;
строчка (линия) в строке заканчивается самим значением, без запятой.
Синтаксис:

stringify(value[, replacer[, spaces_count]])

Параметры:

value: Значение, преобразуемое в строку
replacer: необязательный. Строка – отступ для ключа; Значение по умолчанию – один пробел
spacesCount: необязательный. Число – количество повторов отступа ключа. Значение по умолчанию – 1.

"""
from itertools import count

counter = count()


def stringify(value, replacer=' ', spaces_count=1):
    result = ''
    space = replacer * spaces_count
    if isinstance(value, dict):
        result += ''
        for key, value in value.items():
            if isinstance(value, dict):
                result += f'{space}{key}: {stringify(value, replacer = replacer, spaces_count= spaces_count + 1)}\n'
            else:
                result += '{\n' + f'{space}{key}: {value}\n {space}' + '}'

        return result
    else:
        result += str(value)
    return result
