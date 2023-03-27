import time
from loguru import logger




def logging(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Час виконання функції: {end_time - start_time:.2f} секунд")
        logger.info(f"Результат виконування додавання: {res}")
        return res
    return wrapper


@logging
def calc():
     a = int(input("Введіть значення параметру а:" ))
     b = int(input("Введіть значення параметру а:" ))
     c = int(input("Введіть значення параметру c:" ))
     d = (a + b) * c 
     return d

calc()


