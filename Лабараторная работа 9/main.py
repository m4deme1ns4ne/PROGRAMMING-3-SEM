from typing import Callable, Any
import functools


class MaxCallsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        


class limited_calls():
    def __init__(self, n: int) -> None:
        self.n = n
        self.total = 0

    def __call__(self, func: Callable) -> Any:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            self.total += 1
            if self.total > self.n:
                raise MaxCallsException("Превышено допустимое количество вызовов")
            value = func(*args, **kwargs)
            return value
        return wrapper


@limited_calls(3)
def add(a, b):
    return a + b
    
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)
