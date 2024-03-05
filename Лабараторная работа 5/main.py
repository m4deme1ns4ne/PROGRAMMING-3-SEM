from decorator_all import my_logger
from database_output import database_output


#example
@my_logger('connector_sqlite3')
def even_or_odd(n: int) -> str: 
    return ('Even', 'Odd')[n % 2]


if __name__ == "__main__":
    # even_or_odd(14488)
    database_output(even_or_odd(2131))