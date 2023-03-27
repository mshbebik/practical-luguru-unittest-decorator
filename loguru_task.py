import time
from loguru import logger


def main():
    start_time = time.time()
    a = int(input("Введіть значення параметру а:" ))
    b = int(input("Введіть значення параметру b:" ))
    c = a + b
    end_time = time.time()
    logger.info(f"Маєсо два значення {a} та {b}.")
    logger.info(f"Результат виконування додавання: {c}")
    logger.info(f"Час виконання функції: {end_time - start_time:.2f} секунд")


main()