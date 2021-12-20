from summary_ranges import summary_ranges


def test_find_summary_ranges():
    assert summary_ranges([]) == []
    assert summary_ranges([1]) == []
    assert summary_ranges([1, 2, 3]) == ['1->3']
    assert summary_ranges([0, 1, 2, 7, 5, 6]) == ['0->2', '5->6']
    assert summary_ranges(
        [1, 1, 3, 4, 5, -6, 8, 9, 10, 12, 14, 14],
    ) == ['3->5', '8->10']
    assert summary_ranges(
        [110, 111, 112, 111, -5, -4, -2, -3, -4, -5],
    ) == ['110->112', '-5->-4']
