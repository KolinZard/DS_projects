import numpy as np

def num_rand_game(number: int = 1) -> int:
    """Сначала устанавливаем число равно границам рандом числа // 2, а потом уменьшаем
    границы диапозона поиска в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    low, high = 1, 101 # вынесем границы диапозона рандома числа для удобста f-строк и цикла while
    number = np.random.randint(low, high)
    count = 0

    while True:
        predict = (low + high) // 2 # Делим диапозон числа пополам и делаем вывод: больше или меньше искомого
        count += 1

        if predict == number:
            break
        elif predict < number:
            # Если наше число меньше искомого, меняем  нижний диапозон на наше число +1
            low = predict + 1
        else:
            # Если наше число больше искомого, меняем  верхний диапозон на наше число -1
            high = predict - 1
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