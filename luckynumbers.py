"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    # use while loop to loop for n number of unique random integers
    # while n > 0:
    # find random integer 1-10
    # check if random integer is in generated integer set
    # if not, add random integer to integer list
    # add the random integer to geberated ubteger set
    # decrement n by 1

    # already imported outside of function
    # import random


    generated_integers = set()
    final_integers = []

    while n > 0:
        random_int = random.randint(1, 10)
        if random_int in generated_integers:
            random_int = random.randint(1, 10)
        else:
            generated_integers.add(random_int)
            final_integers.append(random_int)
            n = n - 1

    return final_integers

### Hackbright Solution: ###
### This solution is less frills.
### No need to generate random integer.
### Just randomly choose from list of ints 1-10
### then remove the choice from the list
### Using for - range(n) removes risk of infinite loop (which I experienced).

# def lucky_numbers(n):
#     """Return n unique random numbers from 1-10 (inclusive)."""

#     # START SOLUTION

#     nums = range(1, 11)
#     lucky_nums = []

#     for i in range(n):
#         num = random.choice(nums)
#         nums.remove(num)
#         lucky_nums.append(num)

#     return lucky_nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
