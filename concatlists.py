"""Given two lists, concatenate the second list at the end of the first.

For example, given ``[1, 2]`` and ``[3, 4]``::

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]

It should work if either list is empty::

    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
"""


def concat_lists(list1, list2):
    """Combine lists."""

    # can create new list that is first list, then loop through 2nd list
    # and append on each item in 2nd list,
    ### actually can just loop through 2nd list and append to first list.
    ### do not need 3rd list.
    # but can just combine using the + operator, which combines sequences
    ### this is probably doing the same thing as looping through 2nd list,
    ### append to 1st list under the hood.

    for item in list2:
        list1.append(item)

    return list1

    # return list1 + list2


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
