from mirror_matrix import mirror_matrix


def test_mirror_matrix_return_value():
    assert mirror_matrix([[42]]) is None, (
        "Function shouldn't return anything!"
    )


def test_mirror_matrix():
    empty = []
    mirror_matrix(empty)
    assert empty == []

    empty_row = [
        [],
    ]
    mirror_matrix(empty_row)
    assert empty_row == [[]]

    single_cell = [
        [()],
    ]
    mirror_matrix(single_cell)
    assert single_cell == [[()]]

    text_sample = [
        ['aa', 'bb', 'cc'],
        ['11', '22', '33'],
    ]
    mirror_matrix(text_sample)
    assert text_sample == [
        ['aa', 'bb', 'aa'],
        ['11', '22', '11'],
    ]

    number_sample = [
        [11, 12, 13, 14, 15, 16],
        [21, 22, 23, 24, 25, 26],
        [31, 32, 33, 34, 35, 36],
        [41, 42, 43, 44, 45, 46],
        [51, 52, 53, 54, 55, 56],
        [61, 62, 63, 64, 65, 66],
    ]
    mirror_matrix(number_sample)
    assert number_sample == [
        [11, 12, 13, 13, 12, 11],
        [21, 22, 23, 23, 22, 21],
        [31, 32, 33, 33, 32, 31],
        [41, 42, 43, 43, 42, 41],
        [51, 52, 53, 53, 52, 51],
        [61, 62, 63, 63, 62, 61],
    ]
