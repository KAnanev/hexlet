"""

Реализуйте функцию summary_ranges(), которая находит в списке непрерывные
возрастающие последовательности чисел и возвращает список с их перечислением.

>>> summary_ranges([])
>>>[]
>>> summary_ranges([1])
>>>[]
>>> summary_ranges([1, 2, 3])
>>>['1->3']
>>> summary_ranges([0, 1, 2, 4, 5, 7])
>>>['0->2', '4->5']
>>> summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5])
>>>['110->112', '-5->-4']

"""


def summary_ranges(array):
    result = []
    tmp = []

    if len(array) > 1:
        for i, item in enumerate(array):
            if tmp:
                if tmp[-1] + 1 == item:
                    tmp.append(item)
                else:
                    if len(tmp) > 1:
                        result.append(f'{tmp[0]}->{tmp[-1]}')
                    tmp = []
            else:
                tmp.append(item)
    if len(tmp) > 1:
        result.append(f'{tmp[0]}->{tmp[-1]}')
    return result
