class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_counter = 0
        self.inner_counter = -1
        return self

    def __next__(self):
        if self.outer_counter < len(self.list_of_list):
            sequance = self.list_of_list
            list_out = []
            while sequance:
                element = sequance.pop(-1)
                if isinstance(element, list):
                    sequance.extend(element)
                else:
                    list_out.append(element)
            return list_out.reverse() #, print(list_out)
        else:
            raise StopIteration



def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()