import numpy as np

def num_rand_game(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    predict = np.random.randint(1, 101)
    if predict == number:
        count += 1
        return count
    while predict > number:
        count += 1
        predict -= 10
        if predict == number:
            return count
        while predict < number:
            count += 1
            predict += 1
            if predict == number:
                return count
    while predict < number:
        count += 1
        predict += 10
        if predict == number:
            return count
        while predict > number:
            count += 1
            predict -= 1
            if predict == number:
                return count
            

# print(num_rand_game())


def score_game(num_rand_game) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        num_rand_game ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(num_rand_game(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
score_game(num_rand_game)