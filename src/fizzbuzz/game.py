#!/usr/python3
from functools import reduce
from typing import Tuple


def count_off(index: int) -> str:
    state_index = ('', index)

    if '7' in str(index):
        state, index = rule_contain_7()(state_index)
        return state if state is not '' else str(index)

    if '5' in str(index):
        state, index = rule_contain_5()(state_index)
        return state if state is not '' else str(index)

    if '3' in str(index):
        state, index = rule_contain_3(state_index)
        return state if state is not '' else str(index)

    state, index = rule_cascade_357()(state_index)
    return state if state is not '' else str(index)


def rule_contain_3(state_index: Tuple[str, int]) -> Tuple[str, int]:
    state, index = state_index
    return ('Fizz', index) if '3' in str(index) else ('', index)


def rule_contain_5():
    return pipe(
        is_multiple_of_5,
        is_multiple_of_7
    )


def rule_contain_7():
    return pipe(
        rule_contain_3,
        is_multiple_of_3,
        is_multiple_of_7,
    )


def rule_cascade_357():
    return pipe(
        is_multiple_of_3,
        is_multiple_of_5,
        is_multiple_of_7
    )


def is_multiple_of_3(state_index: Tuple[str, int]) -> Tuple[str, int]:
    state, index = state_index
    return (state + 'Fizz', index) if index % 3 == 0 else (state, index)


def is_multiple_of_5(state_index: Tuple[str, int]) -> Tuple[str, int]:
    state, index = state_index
    return (state + 'Buzz', index) if index % 5 == 0 else (state, index)


def is_multiple_of_7(state_index: Tuple[str, int]) -> Tuple[str, int]:
    state, index = state_index
    return (state + 'Whizz', index) if index % 7 == 0 else (state, index)


def pipe(*func):
    def compose(f, g):
        def h(*args, **kwargs):
            return g(f(*args, **kwargs))

        return h

    return reduce(compose, func)
