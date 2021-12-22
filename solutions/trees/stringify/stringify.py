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
import itertools


# def stringify(value, replacer=' ', spaces_count=1):
#     result = ''
#     level = next(counter)
#     if isinstance(value, dict):
#         result += '{\n'
#         for key, value in value.items():
#             level = next(counter)
#             if isinstance(value, dict):
#                 result += f'{replacer * spaces_count}{key}: {stringify(value, replacer, spaces_count)}'
#             else:
#                 result += f'{replacer * spaces_count * level}{key}: {value}\n'
#         result += '}'
#
#     else:
#         result += str(value)
#     print(level)
#     counter = count(1)
#     return result


# def stringify(data, replacer=' ', spaces_count=1):
#     def inner(items, replacer_in=replacer, count=spaces_count):
#         if not isinstance(items, dict):
#             return str(items)
#         list_values = []
#         for key in items.keys():
#             list_values.append(
#                 ''.join(
#                     [replacer_in * count, str(key), ': ', str(inner(items[key], replacer_in=replacer, count=count + spaces_count,)), ]
#                 )
#             )
#         return '\n'.join(['{', *list_values, '{a}{b}'.format(a=(replacer_in * (count - spaces_count)), b='}'), ])
#
#     return inner(data, replacer_in=replacer, count=spaces_count)

def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


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
    d = stringify(nested, '.')
    print(d)
