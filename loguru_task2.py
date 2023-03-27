import os 
from loguru import logger
import time

# Для того щоб випробувати цю функцію можна вказати шлях на уже дійсні шляхі folder/main.txt aбо folder/notmain.txt

def main():
    try:
        start_time = time.time()
        source_file = input("Введіть шялх файлу з якого хочете дістати інформацію: ")

        with open(f'{source_file}', 'r') as f:
            text = f.read()
            print( 50 * "-")
            logger.info(f"Файл по шляху {source_file} було прочитано та маємо текст: {text}.")
            print( 50 * "-")
    
        finish_file = input("Введіть шлях файлу до якого хочете перенести отриману інформацію: ")

        with open(f'{finish_file}', 'w') as a:
            a.write(text)
        with open(f'{finish_file}', 'r') as c:
            text2 = c.read()
            print( 50 * "-")
            logger.info(f"До файлу по шляху {finish_file} було записано текст: {text2}.")
            print( 50 * "-")
            end_time = time.time()
            print( 50 * "-")
            logger.info(f"Час виконання функції: {end_time - start_time:.2f} секунд")
            print( 50 * "-")
    except:
        print( 50 * "-")
        print("Вказанній шлях не дійсний, спробуйте ще раз")
        print( 50 * "-")
        time.sleep(2)
        main()
main()