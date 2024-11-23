from typing import Callable

from reactivex import operators as ops
from reactivex.subject import BehaviorSubject, Subject


__all__ = (
    "Reducer",
    "Store",

    "create_store"
)


type Reducer[A, S] = Callable[[S, A], S]


class Store[A, S]:
    action: Subject[A]
    state: BehaviorSubject[S]

    def __init__(self, action: Subject[A], state: BehaviorSubject[S]) -> None:
        self.action = action
        self.state = state


def create_store[A, S](
    reducer: Reducer[A, S],
    initial_state: S
) -> Store[A, S]:
    action = Subject()
    state = BehaviorSubject(initial_state)

    action \
        .pipe(ops.map(lambda a: reducer(state.value, a))) \
        .subscribe(state)

    return Store(action, state)
