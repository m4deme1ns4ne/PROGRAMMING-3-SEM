from typing import Callable
import functools
import datetime
from sys import stdout
import json

from database_connection import database_connection


def my_logger(handle='stdout') -> Callable:
    def decorator(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args, **kwargs) -> None:
            d = {
                'datetime': str(datetime.datetime.now()),
                'func_name': str(function.__name__),
                'params': str([*args, *kwargs]),
                'result': str(function(*args, **kwargs))
                }
            if handle == 'stdout':
                stdout.write(json.dumps(d))
            else:
                with open('logger', 'w') as file:
                    json.dump(d, file)
                if handle == 'connector_sqlite3':
                        database_connection(d)
        return wrapper
    return decorator