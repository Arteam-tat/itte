class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_counter = 0
        self.inner_counter = -1
        return self

    def __next__(self):
        self.inner_counter += 1
        if self.inner_counter == len(self.list_of_list[self.outer_counter]):
            self.outer_counter += 1
            self.inner_counter = 0
        if self.outer_counter < len(self.list_of_list):
            return self.list_of_list[self.outer_counter][self.inner_counter]
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()