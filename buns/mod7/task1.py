import functools
import time


def validate_args(func):
    '''Проверяет на корректность переданные аргументы'''

    @functools.wraps(func)
    def wrapped_func(*args):
        if len(args) < 1: return "Not enough arguments"
        if len(args) > 1: return "Too many arguments"
        arg = args[0]
        if type(arg) is not int: return "Wrong types"
        if arg < 0: return "Negative argument"
        return func(*args)

    return wrapped_func


def memoize(func):
    """
    Декоратор, который запоминает в себе аргументы функции
    и возвращаемые значения,
    что повышает производительность
    """
    fib_nums = {}

    @functools.wraps(func)
    def wrap_memoize(*args):
        if args in fib_nums:
            return fib_nums[args]
        else:
            fib_nums[args] = func(*args)
            return fib_nums[args]

    return wrap_memoize


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        execution = end - start
        print(f"Время выполнения функции {func.__name__}: {execution} секунд.")
        return res

    return wrapper


def fibonacci(n):
    '''Функция, которая возвращает число Фибоначи'''
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@validate_args
@timer
def fibonacci_without_memoize(n):
    return fibonacci(n)


@validate_args
@timer
@memoize
def fibonacci_with_memoize(n):
    return fibonacci(n)


print("Без мемоизацией:")
fibonacci_without_memoize(31)

print("\nС мемоизации:")
fibonacci_with_memoize(31)
print()
print(fibonacci.__name__)
print(fibonacci.__doc__)
