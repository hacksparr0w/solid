from typing import Union

import solid


class Inc:
    pass


class Dec:
    pass


Action = Union[Inc, Dec]


def reducer(state: int, action: Action) -> int:
    match action:
        case Inc():
            return state + 1
        case Dec():
            return state - 1


def test() -> None:
    store = solid.create_store(reducer, 0)

    store.action.on_next(Inc())
    store.action.on_next(Inc())
    store.action.on_next(Inc())

    assert store.state.value == 3

    store.action.on_next(Dec())
    store.action.on_next(Dec())

    assert store.state.value == 1
