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
    if isinstance(value, dict):
        result += '{\n'
        for key, value in value.items():
            if isinstance(value, dict):
                result += f'{replacer * spaces_count}{key}: {stringify(value, replacer=replacer, spaces_count=spaces_count + 1)}'
            else:
                result += f'{replacer * spaces_count}{key}: {value}\n'
        result += '}'

    else:
        result += str(value)
    return result


nested = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}


if __name__ == '__main__':
    d = stringify(nested, '-')
    print(d)
