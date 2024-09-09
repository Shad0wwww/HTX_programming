
# Jeg laver en function som tager en anden function som argument 
# og returnerer en ny function som tager en string som argument 
# og returnerer en string. 
# Den nye function skal returnere den string som den anden function
import functools


def uppercase(function):
    def wrapper():
        return function().upper()
    return wrapper


def numberformatter(function):
    def wrapper():
        return '{:,}'.format(function()).replace(',', '.')
    return wrapper

# Jeg laver en function som tager et argument som er et tal
def rounder(decimals: int):
    # Jeg laver en function som tager en anden function som argument
    def decorator(function):
        # Jeg laver en function som tager vilkårlige argumenter og nøgleord og returnerer en værdi
        @functools.wraps(function)
        
        def wrapper(*args, **kwargs):
            return round(function(*args, **kwargs), decimals)
        return wrapper
    return decorator


@uppercase
def hej():
   return 'hej'

@numberformatter
def tal():
    return 123456789

@round(2)
def pi():
    return 3.14159265359

print(hej())
print(tal()) 
print(pi())