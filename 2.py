import types


def flat_generator(list_of_lists):
    outer_counter = 0
    inner_counter = 0
    while outer_counter < len(list_of_lists):
        if inner_counter == len(list_of_lists[outer_counter]):
            outer_counter += 1
            inner_counter = 0
        if outer_counter < len(list_of_lists):
            yield list_of_lists[outer_counter][inner_counter]
        inner_counter += 1
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
