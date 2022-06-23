import numpy as np
import math 


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 # счётчик
    min_num = 1 # минимально возможное число
    max_num = 100 # максимально возможное число
    num = math.floor((min_num+max_num) / 2) # предполагаемое число

    while True:
        count += 1
        if (num == number):
            break  # выход из цикла, если угадали
        if (num > number):
            max_num = math.ceil(((min_num + max_num) / 2))
            num = math.floor((min_num + max_num) / 2)
        else:
            min_num = math.floor((min_num + max_num) / 2) 
            num = math.ceil((min_num + max_num) / 2)
        if (count > 100):
            break

    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
